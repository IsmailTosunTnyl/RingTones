
from flask import request, render_template, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user



main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


