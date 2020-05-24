from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/<name>")
def index(name):
    return render_template("index.html",content=name,teams=["leafs","jays","nords","habs"])


if __name__ == "__main__":
    app.run()
