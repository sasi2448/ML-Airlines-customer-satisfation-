# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:47:15 2020

@author: Sasi
"""

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel('C:/Users/Sasi/Desktop/data science/Machine learning/Capstone/Airline Passenger Satisfaction/data.xlsx')

df = df[(df['Age']<=60)&(df['Departure Delay in Minutes']<=240)&(df['Arrival Delay in Minutes']<=240)&(df['Flight Distance']<=5000)]#cleaing outliers
df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].astype('int')

df2 = pd.get_dummies(df, drop_first=True)


X = df2.drop(['id','satisfaction_v2_satisfied'], axis = 1)
y = df2['satisfaction_v2_satisfied']
rf = RandomForestClassifier(n_jobs =-1)
rf.fit(X,y)
pickle.dump(rf, open('model.pkl','wb'))

