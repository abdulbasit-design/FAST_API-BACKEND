from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["todo_database"]

todos_collection = db["todos"]
users_collection = db["users"]

users_collection.create_index("email", unique=True)
users_collection.create_index("username", unique=True)

print("MongoDB connection successful")