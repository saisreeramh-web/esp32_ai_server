from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('uploading', methods=['POST'])
def upload():
    data = request.data
    print("Received data length:", len(data))
    return jsonify({"response": "Hello from the server!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
