from flask import Flask, request, jsonify
import wave
import io
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def home():
    return "ESP32 AI Server is running!"

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        # Get raw PCM audio from ESP32
        raw_audio = request.data  

        # Save as WAV file
        wav_filename = "recorded.wav"
        with wave.open(wav_filename, 'wb') as wf:
            wf.setnchannels(1)          # mono
            wf.setsampwidth(2)          # 16-bit
            wf.setframerate(16000)      # 16kHz
            wf.writeframes(raw_audio)

        # Speech-to-text
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        print(f"User said: {text}")

        # Here you can connect to AI model (e.g. GPT) 
        # For now just reply simple
        response = f"You said: {text}"
        return jsonify({"response": response})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
