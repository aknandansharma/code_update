from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import json

app = Flask(__name__)
CORS(app)


client = MongoClient("mongodb://localhost:27017/")
db = client["tute_dude_db"]
collection = db["users"]


@app.route('/')
def home():
    return "Backend Running - Flask + MongoDB"


@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json
        print("Received:", data)

        # Validation
        if not data.get('name') or not data.get('email'):
            return jsonify({"error": "All fields required"}), 400

        # Insert into MongoDB
        collection.insert_one(data)

        return jsonify({
            "success": True,
            "message": "Data submitted successfully"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)