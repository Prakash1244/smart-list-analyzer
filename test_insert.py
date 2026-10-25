
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

        result = await collection.insert_one({
            "name": "Buy groceries",
            "completed": False
        })

        print("Document inserted successfully!")
        print("Document ID:", result.inserted_id)

    except Exception as error:
        print(f"Insertion failed: {type(error).__name__}: {error}")

    finally:
        await client.close()

asyncio.run(main())
