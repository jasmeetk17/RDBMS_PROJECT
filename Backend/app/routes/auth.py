# app/routes/auth.py
from flask import Blueprint, request, jsonify
from app.utils.database import get_connection

auth_routes = Blueprint('auth', __name__, url_prefix='/auth')

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=:username AND password=:password", {
        'username': username,
        'password': password
    })
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({"message": "Login successful!", "user_id": user[0]})
    return jsonify({"message": "Invalid credentials"}), 401