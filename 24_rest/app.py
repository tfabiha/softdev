"""
T Fabiha
SoftDev1 pd6
K24 -- A RESTful Journey Skyward
2018-11-13  
"""

import urllib.request
import json

from flask import Flask, render_template
app = Flask(__name__) # create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    j = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=ggxPACCj6D8IeIEilGt5Cs0oGyx7GKeeAXYqmdPP")
    data = j.read()
    #print(data)
    dicts = json.loads(data)
    #print(dicts)

    return render_template("temp.html", pic = dicts["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
