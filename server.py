from flask import Flask, request, jsonify
import wave
import speech_recognition as sr
import openai
import os

app = Flask(__name__)

# ✅ put your real OpenAI API key here
openai.api_key = os.getenv("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")  

@app.route('/')
def home():
    return "sandy is running"

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        # Get raw PCM audio from ESP32
        raw_audio = request.data  

        # Save as WAV
        wav_filename = "recorded.wav"
        with wave.open(wav_filename, 'wb') as wf:
            wf.setnchannels(1)          # mono
            wf.setsampwidth(2)          # 16-bit
            wf.setframerate(16000)      # 16kHz
            wf.writeframes(raw_audio)

        # 🎙️ Speech-to-text
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)
            user_text = recognizer.recognize_google(audio)

        print(f"User said: {user_text}")

        # 🤖 Send to GPT
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system","content":"You are a helpful AI assistant."},
                      {"role":"user","content": user_text}]
        )

        ai_reply = completion.choices[0].message["content"]
        print(f"AI reply: {ai_reply}")

        return jsonify({"response": ai_reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
