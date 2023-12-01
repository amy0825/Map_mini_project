
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from database import add_user, add_loc, logout, User, Location
from authorise import validUname, validEmail, validPass, validRepPss
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import googlemaps

app = Flask(__name__)

gmaps = googlemaps.Client(key='AIzaSyAKkcdsF_5weCl6esnp3rxfelLClTgfSCk')

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

# # refer to main context page
@app.route("/main")
@login_required
def main():
    return render_template("main.html")

# refer to profile page
@app.route("/profile")
@login_required
def profile():
    result = Location.query.filter_by(uid=current_user.id).all()
    return render_template("profile.html", result = result)


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
                return render_template("main.html",username=user)
            else:
                return render_template('login.html', error_message='The password is not match with the account')
        else:
            return render_template('login.html', error_message='This account is not exist, please have a register')

    return render_template("main.html")
# after submit, post data to vertify with database
@app.route('/register/add_new_user', methods =["GET", "POST"])
def getRegisterForm():
     # get input from html form
    uname = request.form.get("username")
    email = request.form.get("email") 
    password = request.form.get("password")
    repPassword = request.form.get("repeated_password") 
    user = User.query.filter_by(email=email).first()

    if user:
        return render_template('register.html', error_message='This email address is exits')
    elif validUname(uname) is False:
        return render_template('register.html', error_message='The username should not contain empty value or space and the length should greate than 4 and less than 8')
    elif validPass(password) is False:
        return render_template('register.html', error_message='The length of password should least 8 characters and least one upper letter')
    elif validEmail(email) is False:
        return render_template('register.html', error_message='The email should not be empty and without the email format')
    elif validRepPss(password, repPassword) is False:
        return render_template('register.html', error_message='Must same with the last password')
    else:
        hash_pwd = generate_password_hash(password)
        add_user(uname,email,hash_pwd)
        return redirect(url_for('login'))



@login_required
@app.route('/get_location', methods=['POST'])
def get_location():
    ip_address = request.form['ip_address']
    api_url = f'http://ip-api.com/json/{ip_address}'
    user_id = current_user.uid
    
    try:
        response = requests.get(api_url)
        data = response.json()
        if data['status'] == 'fail':
            return render_template('main.html', error_message='Invalid IP address')
        else:
            lat = data['lat']
            lon = data['lon']
            location = str(lat)+","+str(lon)
            add_loc(location,user_id)
            return render_template('main.html', result=data, lat=lat, lon=lon)
    except requests.RequestException as e:
        return render_template('main.html', error_message='Error fetching data from the API')


# refer to login page
@app.route("/logout", methods =["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)