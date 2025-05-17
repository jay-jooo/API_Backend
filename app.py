from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Mama mo blue"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').lower()

    if user_input == "hi" or user_input == "hello":
        reply = "Anong maitutulong ko? type kung relationship or other matters"
    elif user_input == "relationship":
        reply = "Wala akong pake. Joke! Anong meron? Type kung breakup,cheating,crush"
    elif user_input == "other matters":
        reply = "Di ko pa masasagot yan eh. Balik ka nalang"
    elif user_input == "breakup" or user_input == "break up":
        reply = "nako be, "
    elif user_input == "bye" or user_input == "paalam":
        reply = "Wag kana babalik"
    elif user_input == "bakit":
        reply = "Aba malay ko."
    elif user_input == "bakit":
        reply = "Aba malay ko."
    else:
        reply = "Sa tingin mo ba alam ko yan?"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)