#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


# In-memory user storage
users = {
    "jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {
        "username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
