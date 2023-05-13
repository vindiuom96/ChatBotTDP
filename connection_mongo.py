from pymongo import MongoClient

def connect_mongo_db():
    CONNECTION_STRING = "mongodb+srv://hitmadulal:root@cluster0.2ctxzy2.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['swinburne']
    return db_Name