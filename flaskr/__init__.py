from flask import Flask
from .db import Database
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['MONGO_URI'] = 'mongodb://root:example@mongodb.youngstorage.in:27017/'
    app.config['MONGO_DBNAME'] = 'youngstorage'

    db = Database()
    db.init_app(app)

    app.register_blueprint(auth)

    @app.teardown_appcontext
    def close_db_connection(exception=None):
        db.close_connection()

    return app
