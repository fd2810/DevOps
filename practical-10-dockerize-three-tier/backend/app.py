from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host="student_database",  # Docker compose service name
        database="studentdb",
        user="postgres",
        password="123456",
        port=5432
    )

# Ensure this exact path matches what the frontend is calling:
@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, course FROM students;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        students = [
            {"id": r[0], "name": r[1], "email": r[2], "course": r[3]}
            for r in rows
        ]
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)