from flask import Blueprint, request, jsonify
from data.records import records

records_bp = Blueprint('records', __name__)

@records_bp.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = next((record for record in records if record['id'] == record_id), None)
    if record:
        return jsonify(record), 200
    return jsonify({"error": "Record not found"}), 404

@records_bp.route('/record', methods=['POST'])
def create_record():
    new_record = request.json
    new_record['id'] = max(record['id'] for record in records) + 1
    records.append(new_record)
    return jsonify(new_record), 201

@records_bp.route('/record', methods=['GET'])
def get_filtered_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)
    filtered = records

    if user_id:
        filtered = [r for r in filtered if r['user_id'] == user_id]
    if category_id:
        filtered = [r for r in filtered if r['category_id'] == category_id]

    if not filtered:
        return jsonify({"error": "No records found"}), 404

    return jsonify(filtered), 200
