
import os
import asyncio
from dotenv import load_dotenv
from pymongo import AsyncMongoClient

load_dotenv()

async def main():
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        print("MONGODB_URI was not found.")
        return

    client = AsyncMongoClient(mongodb_uri)

    try:
        db = client["SmartListDB"]
        collection = db["items"]

        item = await collection.find_one({
            "name": "Buy groceries"
        })

        if item:
            print("Document retrieved successfully!")
            print(item)
        else:
            print("Document not found.")

    except Exception as error:
        print(f"Read failed: {type(error).__name__}: {error}")

    finally:
        await client.close()

asyncio.run(main())
