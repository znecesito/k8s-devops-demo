from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest
import socket
import os

app = Flask(__name__)

# Prometheus metrics
http_requests = Counter(
    "http_requests_total",         # Metric name
    "Total HTTP Requests",         # Description
    ["method", "endpoint"]         # Label names
)


@app.route("/submit", methods=["POST"])
def submit():
    http_requests.labels(method="POST", endpoint="/submit").inc()
    data = request.json
    return jsonify({"status": "received", "data": data})


@app.route("/info")
def info():
    http_requests.labels(method="GET", endpoint="/info").inc()
    return jsonify({
        "container_id": socket.gethostname(),
        "pod_name": os.environ.get("HOSTNAME"),
        "app_version": os.environ.get("APP_VERSION", "dev")
    })


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
