# Frozen Cookies - T. Fabiha && Stefan Tan


from flask import Flask, render_template, request
from util import authenticate
app = Flask(__name__)

user = "bob"
pswd = "bobby"

@app.route("/")
def hello():
	return render_template("login.html")

@app.route("/auth")
def authorization():
    request.cookies.get("username")
    return render_template("authorize.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
