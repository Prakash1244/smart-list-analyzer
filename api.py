from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import analyses_collection
from services import *
import boto3
from fastapi import UploadFile, File
import uuid
from fastapi.responses import StreamingResponse
from io import BytesIO
from botocore.exceptions import ClientError

app = FastAPI()

s3_client = boto3.client(
    "s3",
    region_name="ap-south-1"
)

BUCKET_NAME = "smart-list-reports-unique-number"

class NumberValidate(BaseModel):
    Numbers: list[int]

@app.post('/send-list')
async def send_list_item(data: NumberValidate):
    receive = prepare_analyse(data.Numbers)

    result = await analyses_collection.insert_one(receive)

    return {
        'document': 'Successfully stored',
        '_id': str(result.inserted_id)
    }

@app.get('/get-list')
async def get_all_list():
    result = await retrive_all()

    if result==0:
        raise HTTPException(
            status_code=404,
            detail='Not Found'
        )
    return {
        'document': result
    }

@app.put('/update-docs')
async def update_item(analyse_id: str, data: NumberValidate):
    result = await update_list(analyse_id, data.Numbers)

    if result==0:
        raise HTTPException(
            status_code=404,
            detail='Not Found'
        )
    return {
        'document': 'Successfully updated',
        '_id': analyse_id
    }

@app.delete('/delete-docs')
async def delete_item(analyse_id: str):
    result = await delete_list(analyse_id)

    if result == 0:
        raise HTTPException(
            status_code=404,
            detail='Not Found'
        )
    return {
        'document': 'deleted successfully',
        '_id': analyse_id
    }

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_key = f"{uuid.uuid4()}_{file.filename}"
        s3_client.upload_fileobj(
            file.file,
            BUCKET_NAME,
            file_key
        )

        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "s3_key": file_key
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{file_key}")
async def download_file(file_key: str):
    try:
        response = s3_client.get_object(
            Bucket=BUCKET_NAME,
            Key=file_key
        )

        file_content = response["Body"].read()

        return StreamingResponse(
            BytesIO(file_content),
            media_type=response.get(
                "ContentType",
                "application/octet-stream"
            ),
            headers={
                "Content-Disposition": f'attachment; filename="{file_key}"'
            }
        )

    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete-file/{file_key}")
async def delete_file(file_key: str):
    try:
        s3_client.head_object(
            Bucket=BUCKET_NAME,
            Key=file_key
        )

        s3_client.delete_object(
            Bucket=BUCKET_NAME,
            Key=file_key
        )

        return {
            "message": "File deleted successfully",
            "s3_key": file_key
        }

    except s3_client.exceptions.ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code in ("404", "NoSuchKey", "NotFound"):
            raise HTTPException(
                status_code=404,
                detail="File not found"
            )

        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))