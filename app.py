from flask import Flask , render_template,session
from flask_session import Session

import DB

db = DB.DataBase()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def hello_world():
    data = dict(db.find_user_with_email('mail1','6060'))
    
    return render_template("index.html", data=data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)