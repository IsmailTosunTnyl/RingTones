from flask import Flask , render_template,session,redirect,request,url_for
from flask_session import Session
import sqlite3


# connect sqlite3 database
class DataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db',check_same_thread=False)
        self.c = self.conn.cursor()
    
    def find_user_with_email(self, email,password):
        #dict cursor
        
        query = "SELECT * FROM User WHERE Email = ? AND Password = ?"
        try:
          
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query, (email,password)).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked[0]
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []
    def get_categories(self):
        query = "SELECT * FROM Category"
        try:
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []


db = DataBase()
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"
    return app



@app.route("/")
def index():
    categories = db.get_categories()
    if session.get("user_id") is None:
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
    return render_template("index.html", data=data,categories=categories)

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
    return render_template("signup.html")

@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)