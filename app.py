from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running ✅"

@app.route("/upload", methods=["POST"])
def upload():
    audio_data = request.data  # raw audio from ESP32
    print(f"Received {len(audio_data)} bytes of audio")

    # for now just send a dummy reply
    return jsonify({"reply": "Hello from cloud!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
