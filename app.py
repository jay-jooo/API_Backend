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
        reply = "nako be, This isn't the end of your story, just the close of a chapter. Embrace the pain, and then rise stronger than before. "
    elif user_input == "cheating" or user_input == "cheater":
        reply = "ikalma mo kase their actions say everything about them, and nothing about your worth. You deserve honesty and loyalty. Heal and find someone who truly values you. "
    elif user_input == "crush" or user_input == "happy crush":
        reply = "nge crush palang pala e. gawin mo kausapin mo tas jowain mo na kagad. gagraduate ka na wala ka paring jowa. KUMILOS KANA "
    elif user_input == "walang kwenta" or user_input == "wala kang natulong te":
        reply = "Be wala akong pake, di mo naman ako binabayaran. Try mo premium version ko para mas maganda sagot. 500 lang subscription hahanapan pa kita ng jowa"
    elif user_input == "salamat" or user_input == "thanks":
        reply = "gggg"
    elif user_input == "nge" or user_input == "amp":
        reply = "Sa barangay ka magreklamo."
    elif user_input == "bakit" or user_input == "bat":
        reply = "Aba malay ko."
    elif user_input == "bat di ako crush ng crush ko" or user_input == "bat di niya ko gusto":
        reply = "Aba malay ko. Siguro siya yung problema be, di ikaw. Wag mo masyadong isipin. aral ka muna"
    elif user_input == "bye" or user_input == "ge":
        reply = "osiya lumayas kana"
    else:
        reply = "Sa tingin mo ba alam ko yan? At sa tingin mo ba may pake ako?"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)