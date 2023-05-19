from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['MONGO_URI'] = 'mongodb://root:example@mongodb.youngstorage.in:27017/'
    app.config['MONGO_DBNAME'] = 'youngstorage'

    from . import db

    db.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
