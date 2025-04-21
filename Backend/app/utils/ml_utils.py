import joblib
model = joblib.load('app/ml_model/model_updated.pkl')


def get_recommendations(user_id):
    # dummy: real logic based on model and user profile
    return [{"job_id": 5, "title": "ML Engineer"}]
