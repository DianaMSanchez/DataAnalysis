from flask import Flask

import pandas as pd
data = pd.read_csv("/tripadvisor_restaurants.csv")
app = Flask(__name__)
@app.route("/")



def hora_comida():
    data = pd.read_csv(data)
