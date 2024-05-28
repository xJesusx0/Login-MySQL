from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash
from flask import Blueprint
from Models.models import Users

auth = Blueprint('auth',__name__)

@auth.route("/login", methods=["POST","GET"])
def login():

    if request.method != "POST":
        return render_template("login.html")
    
    users = Users(mysql=auth.mysql)

    username = request.form.get("username")
    password = request.form.get("password")

    response = users.validate_user(username,password)
    
    if response == None:
        flash("Nombre de usuario o contraseña incorrectos")
        return render_template("login.html")

    session["name"] = username
    session["id"] = response[0]

    return redirect("/")     
    
@auth.route("/logout",methods=["GET"])
def logout():
    session["name"] = None
    session["id"] = None
    return redirect("/auth/login")

@auth.route("/register", methods=["GET","POST"])
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

    users = Users(mysql=auth.mysql)
    
    if users.user_exists(username):
        flash("Usuario existente, intenta con otro")
        return render_template("register.html")

    users.register_user(username,password)
    return redirect("/")
