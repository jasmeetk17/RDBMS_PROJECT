from flask import Blueprint, jsonify
from app.utils.ml_utils import get_recommendations

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    recommended_jobs = get_recommendations(user_id)
    return jsonify(recommended_jobs)
