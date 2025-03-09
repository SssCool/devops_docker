from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://192.168.1.44:8090" ##### DEĞİŞTİRRRRR

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/userlist")
def user_list():
    users = requests.get(f"{BACKEND_URL}/list").json()
    return render_template("userlist.html", users=users)

@app.route("/register", methods=["POST"])
def register():
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    requests.post(f"{BACKEND_URL}/register", json=data)
    return "User registered successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)