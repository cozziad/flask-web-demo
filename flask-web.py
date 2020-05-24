from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>yo</h1> Hello World - Home page"

@app.route("/admin/")
def admin():
    return redirect(url_for("home"))

@app.route("/<url_link>")
def catch(url_link):
    return "Sorry. Page " + url_link + " doesn't exist!"

if __name__ == "__main__":
    app.run()
