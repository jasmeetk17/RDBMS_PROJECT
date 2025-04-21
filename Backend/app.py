from flask import Flask
from app.routes import auth, jobs, profile, recommendations

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth.auth_bp)
app.register_blueprint(jobs.jobs_bp)
app.register_blueprint(profile.profile_bp)
app.register_blueprint(recommendations.recommendations_bp)

if __name__ == '__main__':
    app.run(debug=True)
