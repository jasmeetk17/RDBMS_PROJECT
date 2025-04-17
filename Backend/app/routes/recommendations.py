# app/routes/recommendations.py
from flask import Blueprint, jsonify, request
from app.utils.ml_utils import recommend_jobs

recommendation_routes = Blueprint('recommendations', __name__, url_prefix='/recommend')

@recommendation_routes.route('/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommendations = recommend_jobs(user_id)
    return jsonify(recommendations)

