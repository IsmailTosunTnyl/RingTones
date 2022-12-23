from flask import Flask , render_template,session
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


db = DataBase()
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"
    return app



@app.route("/")
def hello_world():
    data = dict(db.find_user_with_email('mail1','6060'))
    
    return render_template("index.html", data=data)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("signin.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)