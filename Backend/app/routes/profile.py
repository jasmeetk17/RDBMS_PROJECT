# app/routes/profile.py
from flask import Blueprint, jsonify, request
from app.utils.database import get_connection

profile_routes = Blueprint('profile', __name__, url_prefix='/profile')

@profile_routes.route('/<user_id>', methods=['GET'])
def get_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = :user_id", {'user_id': user_id})
    profile_data = cursor.fetchone()
    cursor.close()
    conn.close()

    if profile_data:
        return jsonify({
            "user_id": profile_data[0],
            "name": profile_data[1],
            "email": profile_data[2],
            "age": profile_data[3],
        })
    else:
        return jsonify({"error": "Profile not found!"}), 404