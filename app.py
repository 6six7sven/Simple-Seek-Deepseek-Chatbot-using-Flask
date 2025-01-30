from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

@app.route('/')
def index():
    ##return send_from_directory('./templates', 'index.html')
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = requests.post(
        OLLAMA_API_URL,
        json={"prompt": user_input, "model": "deepseek-r1:1.5b"}
    )

    if response.status_code == 200:
        try:
            response_texts = response.text.strip().split('\n')
            responses = [json.loads(text) for text in response_texts]

            # Extract response tokens and join them into a full string
            full_message = "".join(res["response"] for res in responses if "response" in res)

            print("DEBUG: Full backend response:", full_message)  # Debugging line
            return jsonify({"response": full_message})  # Now returning a string
        except json.JSONDecodeError:
            return jsonify({"error": "Failed to decode JSON response", "details": response.text}), 500
    else:
        return jsonify({"error": "Failed to generate response"}), 500

if __name__ == '__main__':
    app.run(debug=True)