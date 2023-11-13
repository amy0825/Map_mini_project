
from flask import Flask, render_template
import requests
from map import get_location


app = Flask(__name__)


# refer home page
@app.route("/")
def home():
    return render_template("index.html")

# refer to login page
@app.route("/login")
def login():
    return render_template("login.html")

# refer to sign up page
@app.route("/register")
def register():
    return render_template("register.html")

# refer to main context page
@app.route("/main")
def main():
    return render_template("main.html")

# refer to profile page
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)