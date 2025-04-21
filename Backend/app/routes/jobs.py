from flask import Blueprint, jsonify

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['GET'])
def get_jobs():
    # Fetch jobs from DB
    return jsonify([{"id": 1, "title": "Frontend Dev"}])
