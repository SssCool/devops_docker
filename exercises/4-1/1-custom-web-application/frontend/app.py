from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Render homepage with links
@app.route('/')
def home():
    return render_template("index.html")

# Render the registration form
@app.route('/register')
def register():
    return render_template("register.html")

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Send data to the .NET backend
    data = {"name": name, "email": email, "password": password}
    response = requests.post("http://my-backend:5001/register", json=data)

    return jsonify(response.json()), response.status_code

# Fetch and display all registered users
@app.route('/users')
def users():
    try:
        response = requests.get("http://my-backend:5001/users")
        users = response.json()
        return render_template("users.html", users=users)
    except requests.exceptions.RequestException:
        return "Error: Unable to fetch users.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
