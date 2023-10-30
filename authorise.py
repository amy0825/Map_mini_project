# all the authorise content will be in this file

# login detail match to the database,successful login create session

# signup detail verify meet to the condition

# logout, session quite


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
        if request.method == "POST":
                # getting input with name = fname in HTML form
                first_name = request.form.get("fname")
                # getting input with name = lname in HTML form 
                last_name = request.form.get("lname") 
                return "Your name is "+first_name + last_name
        return render_template("form.html")