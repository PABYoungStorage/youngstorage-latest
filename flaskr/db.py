from pymongo import MongoClient
from flask import current_app,g
import click

def get_db():
    if 'db' not in g:
        client = MongoClient(current_app.config['MONGO_URI'])
        g.db = client[current_app.config['MONGO_DBNAME']]
    
    return g.db


def init_db():
    db = get_db()

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo("Initialized the database...")

def init_app(app):
    app.cli.add_command(init_db_command)

# class Database:
#     def __init__(self):
#         self.client = None
#         self.db = None

#     def init_app(self, app):
#         self.client = MongoClient(app.config['MONGO_URI'])
#         self.db = self.client[app.config['MONGO_DBNAME']]

#     def get_collection(self,collection_name):
#         return self.db[collection_name]
    
#     def close_connection(self):
#         self.client.close()

# db = Database()