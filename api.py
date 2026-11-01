from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import analyses_collection
from services import *
import boto3
from fastapi import UploadFile, File
import uuid

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