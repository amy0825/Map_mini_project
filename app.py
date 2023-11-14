
from flask import Flask, render_template, request
import requests
from map import get_location
import database
import authorise

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

# # refer to main context page
# @app.route("/main")
# def main():
#     return render_template("main.html")

# refer to profile page
@app.route("/profile")
def profile():
    return render_template("profile.html")

# success login
@app.route('/login/into',methods =["POST"])
def getLoginForm():
    # get input from html form
    uname = request.form.get("username") 
    password = request.form.get("password")
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)