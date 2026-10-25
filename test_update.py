
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

        result = await collection.update_one(
            {"name": "Buy groceries"},
            {"$set": {"completed": True}}
        )

        if result.matched_count:
            print("Document found.")
            if result.modified_count:
                print("Document updated successfully!")
            else:
                print("Document already had this value.")
        else:
            print("Document not found.")

    except Exception as error:
        print(f"Update failed: {type(error).__name__}: {error}")

    finally:
        await client.close()

asyncio.run(main())
