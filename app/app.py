from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the E-commerce Recommendation Engine API!"})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = data.get("user_id", None)

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # Mock recommendation for now
    recommendations = [
        {"product_id": 1, "name": "Wireless Mouse"},
        {"product_id": 2, "name": "Gaming Keyboard"},
        {"product_id": 3, "name": "Bluetooth Headphones"}
    ]

    return jsonify({
        "user_id": user_id,
        "recommended_products": recommendations
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

