from pymongo import MongoClient

# MongoDB Connection Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client['user_database']
users_collection = db['users']
linked_ids_collection = db['linked_ids']
