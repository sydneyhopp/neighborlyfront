from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/")
def hello():
    return jsonify(message="hello from your flask server!")