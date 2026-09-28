from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>MediMate-AI</h1>
    <p>Healthcare Monitoring System is running successfully!</p>
    """


@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "success",
        "message": "MediMate-AI backend is working"
    })


if __name__ == "__main__":
    app.run(debug=True)
    