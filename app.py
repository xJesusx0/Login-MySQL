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

    if request.method != "POST":
        return render_template("login.html")
    
    users = Users(mysql=mysql)

    username = request.form.get("username")
    password = request.form.get("password")

    response = users.validate_user(username,password)
    
    if response == None:
        flash("Nombre de usuario o contraseña incorrectos")
        return render_template("login.html")

    session["name"] = username
    session["id"] = response[0]

    return redirect("/")     
    
    

@app.route("/logout",methods=["GET"])
def logout():
    session["name"] = None
    session["id"] = None
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method != "POST":
        return render_template("register.html")
    
    username = request.form.get("username")  
    confirm_username = request.form.get("confirm-username")

    password = request.form.get("password")  
    confirm_password = request.form.get("confirm-password")

    if username != confirm_username:
        flash("Los nombres de usuario no coinciden")
        return render_template("register.html")

    if password != confirm_password:
        flash("Las contraseñas no coinciden")
        return render_template("register.html")

    users = Users(mysql=mysql)
    
    if users.user_exists(username):
        flash("Usuario existente, intenta con otro")
        return render_template("register.html")

    users.register_user(username,password)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)

