from flask import Flask, request
import speech_recognition as sr
import openai

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    # Save raw audio
    with open("temp.wav", "wb") as f:
        f.write(request.data)

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
    except:
        text = "Could not recognize speech"

    # Generate AI reply
    reply = f"I heard: {text}. I am ChatGPT!"

    return reply

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
