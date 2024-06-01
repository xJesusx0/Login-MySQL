from flask import Flask
from flask import render_template
from flask import session
from flask import redirect
from flask_session import Session
from flask_mysqldb import MySQL
from Blueprints.auth import auth as auth_blueprint

app = Flask(__name__)

app.config.from_object("config.Config")

Session(app)

mysql = MySQL(app)

auth_blueprint.mysql = mysql
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route("/")
def index():
    try:
        if not session["name"]:
            return redirect("/auth/login")
    except KeyError:
        return redirect("/auth/login")
    return render_template("index.html", name = session["name"], modal_message = "Estas seguro de eliminar tu cuenta")

if __name__ == '__main__':
    app.run(debug=True)

