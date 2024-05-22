from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash
from flask_session import Session
from flask_mysqldb import MySQL
from Models.models import Users
app = Flask(__name__)

app.config.from_object("config.Config")

Session(app)

mysql = MySQL(app)

@app.route("/")
def index():
    try:
        if not session["name"]:
            return redirect("/login")
    except KeyError:
        return redirect("/login")
    return render_template("index.html", name = session["name"])

@app.route("/login", methods=["POST","GET"])
def login():

    if request.method == "POST":

        users = Users(mysql=mysql)

        username = request.form.get("username")
        password = request.form.get("password")

        response = users.validate_user(username,password)
    
        if response == None:
            flash("Nombre de usuario o contraseña incorrectos")
            return render_template("login.html")

        session["name"] = username

        return redirect("/") 
    
    return render_template("login.html")

@app.route("/logout",methods=["GET"])
def logout():
    session["name"] = None
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)

