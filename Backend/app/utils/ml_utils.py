import joblib

model = joblib.load(r"C:\Users\Murli mohan\Downloads\Project Rdbms\Backend\app\ml_model\model.pkl")

def recommend_jobs(input_data):
    return model.predict([input_data])
