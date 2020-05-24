from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)

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

@app.route("/<a>")
def fourOhfour(a):
    return render_template("404.html")

#@app.route("/<name>")
#def index(name):
#    return render_template("index.html",content=name,teams=["leafs","jays","nords","habs"])


if __name__ == "__main__":
    app.run(debug=True)
