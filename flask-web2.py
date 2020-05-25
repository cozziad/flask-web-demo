from flask import Flask, redirect,url_for, render_template,request, session,flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "asdfafa43f44rfe"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def slash():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/hobbit")
def hobbit():
    return render_template("hobbit.html")

@app.route("/boss")
def boss():
    return render_template("boss.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        session.permanent = True
        flash("Login success")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Welcome back") 
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html")
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    if "user" in session:
        flash("You have been logged out!","info")
    return redirect(url_for("login"))

@app.route("/<a>")
def fourOhfour(a):
    return render_template("404.html")

#@app.route("/<name>")
#def index(name):
#    return render_template("index.html",content=name,teams=["leafs","jays","nords","habs"])


if __name__ == "__main__":
    app.run(debug=True)
