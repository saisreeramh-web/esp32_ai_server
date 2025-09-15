from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Get API key from Render environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data["text"]

    # Call OpenAI API (GPT-3.5 or GPT-4)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}],
        max_tokens=100
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


