from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask running on Virtual Machine!"

@app.route('/about')
def about():
    return "Deployed successfully on Ubuntu VM"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
