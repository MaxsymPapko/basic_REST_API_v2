from flask import Blueprint, request, jsonify
from data.users import users

users_bp = Blueprint('users', __name__)

@users_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@users_bp.route('/user', methods=['POST'])
def create_user():
    new_user = request.json
    new_user['id'] = max(user['id'] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@users_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": "User deleted"}), 200
