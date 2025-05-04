import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Using motor for async MongoDB connection
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["freelancerExample"]

# COLLECTIONS
user_collection = db["users"]
owner_collection = db["owners"]
