from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from map import get_location
from database import add_user, add_loc, logout, User
from authorise import validUname, validEmail, validPass, validRepPss
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "mySecretKey"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user

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
@login_required
def main():
    return render_template("main.html")

# refer to profile page
@login_required
@app.route("/profile")
def profile():
    return render_template("profile.html")

# success login
@app.route('/login/into',methods =["GET","POST"])
def getLoginForm():
    if request.method == "POST":
        email = request.form.get("username") 
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        # check is user exist
        if user:
            if check_password_hash(user.pwd,password):
                login_user(user)
                return redirect(url_for('main'))
            else:
                print(user.pwd)
                print( generate_password_hash(password))
                return ("<h1>wrong password</h1>")
        else:
            return ("<h1>you need register</h1>")

    return render_template("main.html")

# after submit, post data to vertify with database，获取注册表单的信息
@app.route('/register/add_new_user', methods =["GET", "POST"])
def getRegisterForm():
     # get input from html form
    uname = request.form.get("username")
    email = request.form.get("email") 
    password = request.form.get("password")
    repPassword = request.form.get("repeated_password") 
    user = User.query.filter_by(email=email).first()

    if user:
        return ("<h1>this email address is exits</h1>")
    elif validUname(uname) is False:
        return ("<h1>the username</h1>")
    elif validPass(password) is False:
        return ("<h1>the password</h1>")
    elif validEmail(email) is False:
        return ("<h1>the email</h1>")
    elif validRepPss(password, repPassword) is False:
        return ("<h1>the double password</h1>")
    else:
        hash_pwd = generate_password_hash(password)
        add_user(uname,email,hash_pwd)
        return redirect(url_for('login'))

# refer to login page
@app.route("/logout", methods =["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)