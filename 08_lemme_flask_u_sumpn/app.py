# T. Fabiha
# SoftDev1 pd6
# K08: Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__) # create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)

    link = "<a href='./lance'>lance??</a>"

    return link+"\n\n No hablo queso!"

@app.route("/lance")
def start():
    start2();
    return start2() + "\n\n Lance is my favorite <a href='../paladin' >paladin</a>!!!"
def start2():
    return "Can I have two methods? No. Only the first one runs on its own. :("

@app.route("/paladin")
def hello():
    return "hi <img src='https://fsmedia.imgix.net/4a/41/11/55/ca3f/438d/9e4a/b8a5582cbde1/a-still-of-lance-signing-autographs-in-the-previous-season-of-voltron-legendary-defender-on-netfl.jpeg'>"


if __name__ == "__main__":
    app.debug = True
    app.run()
