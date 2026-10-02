from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg

app = Flask(__name__)
CORS(app)

# PostgreSQL connection
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "studentdb2",
    "user": "postgres",
    "password": "123456"
}


def get_connection():
    return psycopg.connect(**DB_CONFIG)


@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API is running"
    })


@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, email, course FROM students ORDER BY id"
    )

    students = cur.fetchall()

    cur.close()
    conn.close()

    result = []

    for student in students:
        result.append({
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "course": student[3]
        })

    return jsonify(result)


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO students (name, email, course)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (name, email, course)
    )

    student_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": "Student added successfully",
        "id": student_id
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)