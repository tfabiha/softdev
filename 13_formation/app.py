# T. Fabiha
# Softdev1 pd6
# HW13
# 2018-09-28

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	print(app)
	return render_template("form.html")

@app.route("/auth")
def authenticate():
	print(app)
	print(request)
	print(request.args)
	print(request.args["username"])
	print(request.method)
	return render_template("greeting.html",
							name = request.args['username'],
							method = request.method)

if __name__ == "__main__":
	app.debug = True
	app.run()
