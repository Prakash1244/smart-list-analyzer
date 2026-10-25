
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

        result = await collection.delete_one({
            "name": "Buy groceries"
        })

        if result.deleted_count:
            print("Sample document deleted successfully!")
        else:
            print("No matching document was found.")

    except Exception as error:
        print(f"Delete failed: {type(error).__name__}: {error}")

    finally:
        await client.close()

asyncio.run(main())
