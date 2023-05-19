from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        self.client = MongoClient(app.config['MONGO_URI'])
        self.db = self.client[app.config['MONGO_DBNAME']]

    def get_collection(self,collection_name):
        return self.db[collection_name]
    
    def close_connection(self):
        self.client.close()

db = Database()