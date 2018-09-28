# Cactipie - Kyle Tau && T. Fabiha
# SoftDev1 pd6
# K10: Jinja Tuning ...
# 2018-09-24

import random
from util import occupations as occ
from flask import Flask, render_template

app = Flask(__name__) # create instance of class Flask

@app.route("/occupations") #assign fxn to route
def hello_world():
    return render_template("template_html.html",
                            title = "Occupations",
                            rand_occ = occ.occChooser(occDict),
                            dict = occDict)

occDict = occ.dictFile("./data/occupations.csv")

if __name__ == "__main__":
    app.debug = True
    app.run()
