from flask import Flask
from prometheus_client import Counter, start_http_server

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello! Flask application is running."

@app.route("/hello")
def hello():
    REQUEST_COUNT.inc()
    return "Hello from the monitoring application!"

if __name__ == "__main__":
    start_http_server(8000)   # Prometheus metrics endpoint
    app.run(host="0.0.0.0", port=5000)
