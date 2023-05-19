import functools
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash,generate_password_hash
import json
from .db import get_db

auth_bp = Blueprint('auth', __name__,url_prefix="/auth")

@auth_bp.route('/signin', methods=['GET'])
def login():
    # Access the users collection
    db = get_db()
    users_collection = db['users']

    # Authentication logic...
    # Example: Verify username and password
    # data = request.get_json()
    # username = data.get('username')
    # password = data.get('password')

    users = list(users_collection.find())
     # Serialize the result to JSON
    users_json = json.dumps(users, default=str)
    if users:
         # Return the JSON response
        return users_json, 200, {'Content-Type': 'application/json'}
    else:
        # Login failed
        return jsonify({'message': 'Invalid username or password'}), 401
    

@auth_bp.route('/signup', methods=['POST'])
def register():
    # Access the users collection
    
    # Registration successful
    return jsonify({'message': 'Registration successful'})

@auth_bp.route('/signout', methods=['GET'])
def logout():
    # Logout logic...
    return jsonify({'message': 'Logout successful'})

