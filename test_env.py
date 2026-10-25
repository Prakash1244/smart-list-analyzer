
import os
from dotenv import load_dotenv

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

if mongodb_uri:
    print("MongoDB connection string loaded successfully.")
else:
    print("MONGODB_URI was not found. Check your .env file.")
