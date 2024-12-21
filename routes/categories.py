from flask import Blueprint, request, jsonify
from data.categories import categories

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/category', methods=['GET'])
def get_categories():
    return jsonify(categories), 200

@categories_bp.route('/category', methods=['POST'])
def create_category():
    new_category = request.json
    new_category['id'] = max(category['id'] for category in categories) + 1
    categories.append(new_category)
    return jsonify(new_category), 201

@categories_bp.route('/category', methods=['DELETE'])
def delete_category():
    category_id = request.args.get('id', type=int)
    global categories
    categories = [category for category in categories if category['id'] != category_id]
    return jsonify({"message": "Category deleted"}), 200
