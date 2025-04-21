from flask import Blueprint, request, jsonify

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    return jsonify({"id": user_id, "name": "Alice"})

@profile_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.get_json()
    return jsonify({"message": "Profile updated!"})
