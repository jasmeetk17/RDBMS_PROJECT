import pickle

# Load model
model = pickle.load(open('app/ml_model/model.pkl', 'rb'))

def get_recommendations(user_id):
    # dummy: real logic based on model and user profile
    return [{"job_id": 5, "title": "ML Engineer"}]
