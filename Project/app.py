from flask import Flask , render_template,session,redirect,request,url_for
from flask_session import Session
import sqlite3
import 


    


db = DataBase()
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"
    return app

# ************************** Routes **************************
alerts = [1,]
@app.route("/")
def index():
    
    tempalert = alerts
    if alerts[0]:
        alerts[0] = 0
    
    
    
    categories = db.get_categories_count()
    ringtones = db.get_ringtones()
    if session.get("user_name") is None:
        data = {
            "Name": "Sign In",
            "Email": "Sign In",   
        }
        
    else:
        data = {
            "Name": session["user_name"],
            "Email": session["user_email"], 
        }
    print(data)
    print(session)
    return render_template("index.html", data=data,categories=categories,ringtones=ringtones,alerts=tempalert)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get('email')
        
        password = request.form.get('password')
        print(email,password)
        print('---')
        data = db.find_user_with_email(email,password)
        if data:
            session["user_id"] = data["Id"]
            session["user_name"] = data["Name"]
            session["user_email"] = data["Email"]
            print(session)
            return redirect(url_for('index'))
        else:
            return render_template("signin.html", message="Invalid Email or Password")
    
    email = request.form.get("floatingInput")
    password = request.form.get("floatingPassword")
    print(email,password)
    print('***')
    return render_template("signin.html",message="Welcome")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name=request.form.get("signUpName")
        email=request.form.get("signUpEmail")
        password=request.form.get("signUpPassword")
        db.add_user(name,email,password)
        session["user_name"] = name
        session["user_email"] = email
        data = db.find_user_with_email(email,password)
        session["user_id"] = data["Id"]
        print(session)
        return redirect(url_for("index"))
    return render_template("signup.html")

@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for('index'))

# add item to cart
@app.route("/add_to_cart/<id>", methods=["POST", "GET"])
def add_to_cart(id):
    global alerts
    alerts = [1,]
    if session.get("user_name") is None:
        return redirect(url_for('signin'))
    else:    
        print('----******************************* ',id)
        #  show succes message and redirect to cart page
        
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)