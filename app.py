# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:00:20 2020

@author: Sasi
"""



from flask import Flask, request
import pickle
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)


pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Post"])
def predict():
    
    """Let's Predict Customer satisfaction  
    Airlines Passesnger satisfaction
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Flight Distance
        in: query
        type: number
        required: true
      - name: Seat comfort
        in: Rating from 0 to 5
        type: number
        required: true
      - name: Departure/Arrival time convenient
        in: query
        type: number
        required: true
      - name: Food and drink
        in: query
        type: number
        required: true
      - name: Gate location
        in: query
        type: number
        required: true
      - name: Inflight wifi service
        in: query
        type: number
        required: true
      - name: Inflight entertainment
        in: query
        type: number
        required: true
      - name: Online support
        in: query
        type: number
        required: true
      - name: Ease of Online booking
        in: query
        type: number
        required: true
      - name: On-board service
        in: query
        type: number
        required: true
      - name: Leg room service
        in: query
        type: number
        required: true
      - name: Baggage handling
        in: query
        type: number
        required: true
      - name: Checkin service
        in: query
        type: number
        required: true
      - name: Cleanliness
        in: query
        type: number
        required: true
      - name: Online boarding
        in: query
        type: number
        required: true
      - name: Departure Delay in Minutes
        in: query
        type: number
        required: true
      - name: Arrival Delay in Minutes
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
      - name: Customer type
        in: query
        type: number
        required: true
      - name: Type of Travel
        in: query
        type: number
        required: true
      - name: Class
        in: query
        type: number
        required: true
      - name: Class_Ecoplus
        in: query
        type: number
        required: true
    responses:
        200:
            description: 
        
    """
    f1=request.args.get("Age")
    f2=request.args.get("Flight Distance")
    f3=request.args.get("Seat comfort")
    f4=request.args.get("Departure/Arrival time convenient")
    f5=request.args.get("Food and drink")
    f6=request.args.get("Gate location")
    f7=request.args.get("Inflight wifi service")
    f8=request.args.get("Inflight entertainment")
    f9=request.args.get("Online support")
    f10=request.args.get("Ease of Online booking")
    f11=request.args.get("On-board service")
    f12=request.args.get("Leg room service")
    f13=request.args.get("Baggage handling")
    f14=request.args.get("Checkin service")
    f15=request.args.get("Cleanliness")
    f18=request.args.get("Online boarding")
    f19=request.args.get("Departure Delay in Minutes")
    f20=request.args.get("Arrival Delay in Minutes")
    f21=request.args.get("Gender")
    f22=request.args.get("Customer type")
    f23=request.args.get("Type of Travel")
    f24=request.args.get("Class")
    f25=request.args.get("Class_Ecoplus")
    d = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f18,f19,f20,f21,f22,f23,f24,f25]
    
    
    
    prediction=model.predict([d])
    if prediction[0] == 0:
        output = 'Airline passenger is not satisfied'
    elif prediction[0] == 1:
        output = 'Airline passenger is satisfied'
    return output
    
    

if __name__=='__main__':
    app.run()