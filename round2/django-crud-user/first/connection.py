from pymongo import MongoClient

def get_mongo_client():

    try:
        client = MongoClient('mongodb://localhost:27017/')
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None 