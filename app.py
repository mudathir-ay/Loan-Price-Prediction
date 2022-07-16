from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model_svm.pkl", "rb"))



@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method=="POST":
        #Get Gender
        Gender=request.form['Gender']
        if (Gender=="Male"):
            Gender=1
        else:
            Gender=0
        #Get marital status
        Married=request.form['Married']
        if( Married=="Yes"):
            Married=1
        else:
            Married=0
        #Get number of dependents 
        Dependents=request.form['Dependents']
        if(Dependents=="0"):
            Dependents=0
        elif(Dependents=="1"):
            Dependents=1
        elif(Dependents=="2"):
            Dependents=2
        else:
            Dependents=4
        #Get Education 
        Education=request.form['Education']
        if( Education=='Graduate'):
            Education=1
        else:
            Education=0
        #Get employment 
        Self_Employed=request.form['Self_Employed']
        if(Self_Employed=="Yes"):
            Self_Employed=1
        else:
            Self_Employed=0
        #Get Application income 
        ApplicantIncome=int(request.form['ApplicantIncome'])
        #Get Coapplicant income 
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        #Get Loan Amount
        LoanAmount=float(request.form['LoanAmount'])
        #Get Loan Amount Term 
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
        #Get Credit History
        Credit_History=float(request.form['Credit_History'])
        #Get Property Area 
        Property_Area=request.form['Property_Area']
        if(Property_Area=='Rural'):
            Property_Area=0
        elif(Property_Area=='Semiurban'):
            Property_Area=1
        else:
            Property_Area=2
        prediction=model.predict([[Gender, Married, Dependents, Education,Self_Employed,ApplicantIncome, CoapplicantIncome,LoanAmount,Loan_Amount_Term,
        Credit_History, Property_Area]])
        final_pred=prediction[0]
        if (final_pred==0):
            pred_text="Loan Denied"
        else:
            pred_text="Loan Granted"
        return render_template("index.html", prediction_text=pred_text)
    
    return render_template("index.html")
if __name__ == "__main__":
    app.run(port=5000,debug=True)


