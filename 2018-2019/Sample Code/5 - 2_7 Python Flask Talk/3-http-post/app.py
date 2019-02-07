from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = []


@app.route("/")
def index():
    return render_template("index.html", users=users)


@app.route("/add", methods=["POST"])
def add():
    users.append(request.form["username"])
    return redirect("/")


app.run(debug=True)
