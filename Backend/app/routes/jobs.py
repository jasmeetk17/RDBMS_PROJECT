# app/routes/jobs.py
from flask import Blueprint, jsonify
from app.utils.database import get_connection

jobs_routes = Blueprint('jobs', __name__, url_prefix='/jobs')

@jobs_routes.route('/', methods=['GET'])
def get_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT job_id, job_role, company, location FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()

    job_list = [
        {"job_id": job[0], "role": job[1], "company": job[2], "location": job[3]}
        for job in jobs
    ]
    return jsonify(job_list)