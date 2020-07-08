import numpy as np
import sys
import pandas as pd
import warnings
#import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv('test.csv')

#import sys
#from sys import argv
#print(first arsys.argv[1])

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

import sys
value=sys.argv[1]
print("Predicting value for ===", value)

#The predict() method takes a 2d array of values you want to predict on
test=reg.predict(np.array([int(value)]).reshape(1,1))

