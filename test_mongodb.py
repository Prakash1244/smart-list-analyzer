
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
        await client.admin.command("ping")
        print("Successfully connected to MongoDB Atlas!")
    except Exception as error:
        print(f"Connection failed: {type(error).__name__}: {error}")
    finally:
        await client.close()

asyncio.run(main())
