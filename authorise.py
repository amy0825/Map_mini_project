import re

# use with register
# 1. the username should not contain empty value or space and the length should greate than 4 and less than 8
def validUname(uname):
        if not uname or ' ' in uname or len(uname) < 5 or len(uname) > 7:
                return False
        return True
# 2. the length of password should least 8 characters and least one upper letter
def validPass(password):
        if len(password) < 8 or not any(char.isupper() for char in password):
                return False
        return True

# 3. the email should not be empty and without the email format
def validEmail(email):
        if not email:
                return False

        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(re.match(email_pattern, email))

# 4. check two password are same in hash 
def validRepPss(password1, password2):
        if password1 == password2:
                return True
        return False
