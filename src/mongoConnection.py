from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.credentials import MONGO_PASS

uri = f"mongodb+srv://onferreira:{MONGO_PASS}@cluster0.e2s1ofa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.dio_live

trends_collection = db.trends
