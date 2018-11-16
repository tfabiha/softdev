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
def home():
    return render_template("home.html")

@app.route("/dictionary")
def dictionaryapi():

    ##########################
    ### MERRIAM-DICTIONARY ###
    ##########################
    url_base = "https://www.dictionaryapi.com/api/v3/references/spanish/json/"

    word = "hello"
    key = "ae5e1940-834e-4d07-b3ac-22c4d8937ffc"

    url = url_base
    url += word
    url += "?key=" + key

    print(url)

    j = urllib.request.urlopen(url)
    data = j.read()
    e_dicts = json.loads(data)
    print(e_dicts)

    word = "comer"
    key = "ae5e1940-834e-4d07-b3ac-22c4d8937ffc"

    url = url_base
    url += word
    url += "?key=" + key

    print(url)

    j = urllib.request.urlopen(url)
    data = j.read()
    s_dicts = json.loads(data)
    print(s_dicts)


    return render_template("dictionary.html",
                            e_word = e_dicts[0]["meta"]["id"],
                            e_language = e_dicts[0]["meta"]["lang"],
                            e_pos = e_dicts[0]["fl"],
                            e_translation = e_dicts[0]["shortdef"][0],
                            s_word = s_dicts[0]["meta"]["id"],
                            s_language = s_dicts[0]["meta"]["lang"],
                            s_pos = s_dicts[0]["fl"],
                            s_translation = s_dicts[0]["shortdef"][0])

@app.route("/cats")
def cats():
    url = "https://aws.random.cat/meow"
    print(url)

    cats = []

    for i in range(3):

        j = urllib.request.urlopen(url)
        data = j.read()
        cat_url = json.loads(data)
        cats.append(cat_url["file"])

    print(cats)
    return render_template("cats.html", kitty = cats)

@app.route("/bored")
def bored():
    url = "https://www.boredapi.com/api/activity"
    print(url)


    j = urllib.request.urlopen(url)
    data = j.read()
    bored = json.loads(data)

    print(bored)
    return render_template("bored.html",
                            activity = bored["activity"],
                            type = bored["type"],
                            participants = bored["participants"])

if __name__ == "__main__":
    app.debug = True
    app.run()
