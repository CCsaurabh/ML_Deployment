# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:11:21 2021

@author: SaurabhM
"""


# importing the required libraries
from flask import Flask, render_template, request, redirect, url_for
from joblib import load

import pandas as pd
# load the pipeline object
pipeline = load("loan_predict.joblib")

# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents = int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        ApplicantIncome = int(request.form['ApplicantIncome'])
        CoapplicantIncome = int(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        Credit_History = float(request.form['Credit_History'])
        Property_Area=int(request.form['Property_Area'])
    data={'gender':Gender,'Married':[Married],'Dependents':[Dependents],'Education':[Education],'Self_Employed':[Self_Employed],'ApplicantIncome':[ApplicantIncome],'CoapplicantIncome':[CoapplicantIncome],'LoanAmount':[LoanAmount],'Loan_Amount_Term':[Loan_Amount_Term],'Credit_History':[Credit_History],'Property_Area':[Property_Area]} 
    
    df = pd.DataFrame(data) 
    
    
    value=pipeline.predict(df)


    return render_template('home.html',Gender=Gender,result=value)
"""
# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)) + " </xmp> """


if __name__=="__main__":
    app.run()