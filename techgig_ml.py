# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

from pandas.tools.plotting import scatter_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np 
import pandas as pd 
testfile = "input/test_data.csv"
activity_file = "input/invesco/Code-Gladiators-Activity.csv"
aum_file = "input/invesco/Code-Gladiators-AUM.csv"
iexp_file = "input/invesco/Code-Gladiators-InvestmentExperience.csv"
transaction_file = "input/invesco/Code-Gladiators-Transaction.csv"

aum = pd.read_csv(aum_file,sep=",")
activity = pd.read_csv(activity_file,sep=",")
iexp = pd.read_csv(iexp_file,sep=",")
transaction = pd.read_csv(transaction_file,sep=",")

testData = pd.read_csv(testfile,sep=",")

print(activity.info())
print(aum.info())
print(iexp.info())
print(transaction.info())

print(transaction.groupby("Transaction_Type").size())

null_activity_columns=activity.columns[activity.isnull().any()]
print(null_activity_columns)


#fill na value of float/int objects with median
#trainData['LoanAmount'].fillna(trainData["LoanAmount"].median(), inplace=True)
#testData['LoanAmount'].fillna(testData["LoanAmount"].median(), inplace=True)
#
#trainData['Loan_Amount_Term'].fillna(trainData["Loan_Amount_Term"].median(), inplace=True)
#testData['Loan_Amount_Term'].fillna(testData["Loan_Amount_Term"].median(), inplace=True)
#
#trainData['Credit_History'].fillna(trainData["Credit_History"].median(), inplace=True)
#testData['Credit_History'].fillna(testData["Credit_History"].median(), inplace=True)
#
#
#from sklearn.preprocessing import LabelEncoder
#
#labelEnc=LabelEncoder()
#
#cat_vars=['Gender','Married','Dependents', 'Education', 'Self_Employed','Property_Area']
#
#for col in cat_vars:
#    trainData[col]=labelEnc.fit_transform(trainData[col].astype('str'))
#    testData[col]=labelEnc.fit_transform(testData[col].astype('str'))
#
#trainData['Gender'].fillna(trainData["Gender"].median(), inplace=True)
#testData['Gender'].fillna(testData["Gender"].median(), inplace=True)
    
#select_top = SelectKBest(score_func=chi2, k = 7)
#fit = select_top.fit(X,Y)
#features = fit.transform(X)
#print(features[0:5])
#
#print(trainData.head())
#
##Shows top 5 features are 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
#X_features = pd.DataFrame(data = features, columns = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History'])
#
#X_features.head()
#
#from sklearn.preprocessing import StandardScaler
#rescaledX = StandardScaler().fit_transform(X_features)
#X = pd.DataFrame(data = rescaledX, columns= X_features.columns)

#print(X.head())

#validation_size = 0.20
#seed = 6
#X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
#
#scoring = 'accuracy'
##Algos are binary classfier
#print(X_validation.columns) 
##LDA is giving better result
#clf = LogisticRegression()
#clf.fit(X_train, Y_train)
#test_id = testData['Application_ID']
#preds = clf.predict(testData[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
#       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
#       'Loan_Amount_Term', 'Credit_History']])
#
#print(len(preds))
#out_df = pd.DataFrame({"Application_ID":test_id, "Loan_Status":preds})
#print(out_df[200:250])
#file = out_df.to_csv("techgig_submission.csv", index=False)

