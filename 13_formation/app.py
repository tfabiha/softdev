from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	print(app)
	return "hi"

@app.route("/auth")
def authenticate():
	print(app)
	print(request)
	print(request.args)
	return "WAAA"

if __name__ == "__main__":
	app.debug = True
	app.run()
