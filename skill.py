from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alexa', methods=['POST'])
def alexa():
    data = request.json
    intent = data['request']['intent']['name']
    if intent == "ProductRecommendationIntent":
        return jsonify({"response": "Here are some products you might love!"})
    elif intent == "OrderStatusIntent":
        return jsonify({"response": "Your order is on the way!"})
    return jsonify({"response": "Sorry, I didn't get that."})