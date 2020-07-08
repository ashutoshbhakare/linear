import numpy as np
from flask import Flask, request, render_template
app = Flask(__name__)

import pandas as pd
import warnings
from sklearn import linear_model

df=pd.read_csv('test.csv')

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

@app.route("/")
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    value1=request.form['flatarea']
    test=reg.predict(np.array([int(value1)]).reshape(1,1))
    return 'Your Flat Value would be : {}'.format(test)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
