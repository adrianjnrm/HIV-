from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "en": {
        "malaria": "You may have malaria. Please get tested at a nearby clinic.",
        "cough": "It may be a cold or respiratory infection. Monitor your symptoms.",
        "unknown": "I'm not sure. Please describe more symptoms or consult a healthcare provider."
    },
    "sw": {
        "malaria": "Huenda una malaria. Tafadhali nenda kupimwa katika kliniki ya karibu.",
        "cough": "Huenda ni mafua au maambukizi ya kupumua. Fatilia dalili zako.",
        "unknown": "Sielewi vizuri. Tafadhali eleza zaidi au wasiliana na mhudumu wa afya."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['message'].lower()
    lang = data.get('lang', 'en')

    if "fever" in user_input and "headache" in user_input:
        reply = responses[lang]["malaria"]
    elif "cough" in user_input:
        reply = responses[lang]["cough"]
    else:
        reply = responses[lang]["unknown"]

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
