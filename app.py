from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running ✅"

@app.route("/upload", methods=["POST"])
def upload():
    return jsonify({"status": "ok", "message": "Audio received!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
