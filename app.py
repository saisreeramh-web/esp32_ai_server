from flask import Flask, request, jsonify
import speech_recognition as sr
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "✅analysing sandy"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files['file']
    recognizer = sr.Recognizer()

    with sr.AudioFile(io.BytesIO(audio_file.read())) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            reply = f"I heard you say: {text}. My name is Sandy 🤖"
        except Exception as e:
            reply = f"❌ Could not recognize: {str(e)}"

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
