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
    '''
    j = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=ggxPACCj6D8IeIEilGt5Cs0oGyx7GKeeAXYqmdPP")
    data = j.read()
    #print(data)
    dicts = json.loads(data)
    #print(dicts)
    '''

    url_base = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"

    '''
    the url takes the following variables
    Note: this example is with [COUNTRY]
          another option [BASIN] is available

    type: mavg => Monthly average
          annualavg => Annual average
          manom => Average monthly change (anomaly)
          annualanom => Average annual change (anomaly).

    NOTE: * GCM AND SRES ARE OPTIONAL
          * THEY ARE INCLUDED IN THIS EXAMPLE TO REDUCE THE AMOUNT OF OUTPUT TAKEN
            AND STREAMLINE THE SOLUTION
          * IF YOU INCLUDE NEITHER YOU WILL HAVE A 30-OBJECT RESPONSE
          * IF YOU HAVE GCM ONLY YOU WILL HAVE A 2-OBJECT RESPONSE
          * IF YOU HAVE SRES ONLY YOU WILL HAVE A 15-OBJECT RESPONSE

    NOTE: General Circulation Models (GCM) are the models used to simulate
          the global climate system

    [OPTIONAL] GCM: bccr_bcm2_0
                    csiro_mk3_5
                    ingv_echam4
                    cccma_cgcm3_1
                    cnrm_cm3
                    gfdl_cm2_0
                    gfdl_cm2_1
                    ipsl_cm4
                    microc3_2_medres
                    miub_echo_g
                    mpi_echam5
                    mri_cgcm2_3_2a
                    inmcm3_0
                    ukmo_hadcm3
                    ukmo_hadgem1

    NOTE: Special Report on Emissions Scenarios (SRES) are possible scenarios of
          gas emissions

    [OPTIONAL] SRES: a2
                     b1

    var: pr => Precipitation (rainfall and assumed water equivalent), in millimeters
         tas => Temperature, in degrees Celsius

    (start, end) [ONLY POSSIBLE COMBINATIONS]
        Past: (1920, 1939)          Future: (2020, 2039)
              (1940, 1959)                  (2040, 2059)
              (1960, 1979)                  (2060, 2079)
              (1980, 1999)                  (2080, 2099)

    IS03: country code
    '''

    type = "mavg"
    GCM = "bccr_bcm2_0"
    SRES = "a2"
    var = "tas"
    start = "2020"
    end = "2039"
    IS03 = "usa"

    url = url_base
    url += type + "/"
    url += GCM + "/"
    url += SRES + "/"
    url += var + "/"
    url += start + "/"
    url += end + "/"
    url += IS03

    if SRES == "pr":
        suff = " mm"
    else:
        suff = " C"

    print(url)

    j = urllib.request.urlopen(url)
    data = j.read()
    dicts = json.loads(data)[0]
    print(dicts)

    return render_template("temp.html",
                            scen = dicts["scenario"],
                            g = dicts["gcm"],
                            variable = dicts["variable"],
                            f = dicts["fromYear"],
                            e = dicts["toYear"],
                            months = dicts["monthVals"],
                            s = suff)

if __name__ == "__main__":
    app.debug = True
    app.run()
