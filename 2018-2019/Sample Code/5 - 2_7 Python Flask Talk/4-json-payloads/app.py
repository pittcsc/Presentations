from flask import Flask, request, jsonify

app = Flask(__name__)

users = []


@app.route("/users")
def list_users():
    return jsonify({
        "users": users,
    })


@app.route("/users", methods=["POST"])
def add_user():
    users.append(request.json["username"])
    return jsonify({
        "users": users,
    })


app.run(debug=True)
