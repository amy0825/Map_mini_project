from flask import Flask, request, render_template
import requests

auth = Flask(__name__)

# all the authorise content will be in this file

# login detail match to the database,successful login create session

# use with register
# 1. 检查名字长度，不能空值，不能有空格，大于四位数，小于八位数
def validUname(uname):
        return  True
# 2. 检查密码，长度不能少于8位数，要有一个大写符号
def validPass(password):
        return  True

# 3. 检查邮箱，有一个专门检查是不是邮箱的函数
def validEmail(email):
        return True

# 4. 检查两个次密码输入，是否相同
def validRepPss(password1, password2):
        return True

# check does login details in the database
# 5. 检查用户名是否在数据库,密码是否相同
def validDB(uname,pwd):
        return True

# signup detail verify meet to the condition

# ----------------------------------------------------------------------------------
# logout, session quite


# after submit, post data to vertify with database，获取注册表单的信息
@auth.route('/register/add_new_user', methods =["POST"])
def getRegisterForm():
        # get input from html form
        uname = request.form.get("username")                
        email = request.form.get("email") 
        password = request.form.get("password")
        repPassword = request.form.get("repeated_password") 
        # 验证全都通过，注册成功，写入数据库
        if (validUname(uname) and validPass(password) and validEmail(email) and validRepPss(repPassword)):
                # 连接数据库fun
                # 加入数据库fun
                return

@auth.route('/login/into',methods =["POST"])
def getLoginForm():
        # get input from html form
        uname = request.form.get("username") 
        password = request.form.get("password")
        
  
# 从database.py导入连接数据库，添加数据functions
# 连接数据库fun
# def connect():
#         if(validUname and validPass and validEmail and validRepPss):
#                 # session connect.
#         return 

# 1. session start，获得当前用户名
# 2. session close，退出当前账号，清理缓存
# 