from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "service": "dokploy-test-pipeline",
        "status": "running",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "message": "v2 - Auto-deploy pipeline verified!"
    })

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
