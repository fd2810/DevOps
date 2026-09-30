from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my first Flask API",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
