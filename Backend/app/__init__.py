from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.auth import auth_routes
    from app.routes.jobs import jobs_routes
    from app.routes.profile import profile_routes
    from app.routes.recommendations import recommendation_routes

    app.register_blueprint(auth_routes)
    app.register_blueprint(jobs_routes)
    app.register_blueprint(profile_routes)
    app.register_blueprint(recommendation_routes)

    return app
