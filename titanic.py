# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:10:36 2017

@author: Ratnesh
"""

# -*- coding: utf-8 -*-
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from pandas.tools.plotting import scatter_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np 
import pandas as pd 
testfile = "input/test_data.csv"
trainfile = "input/train_data.csv"
trainData = pd.read_csv(trainfile,sep=",")
testData = pd.read_csv(testfile,sep=",")

print(trainData.info())
print(trainData.groupby('Loan_Status').size())

trainData = trainData.drop(['Application_ID'],axis=1)

null_columns=trainData.columns[trainData.isnull().any()]
print(null_columns)
print(trainData.isnull().sum())
print(testData.isnull().sum())
print(trainData.columns)                               
trainData.hist(figsize=(10,10))

#fill na value of float/int objects with median
trainData['LoanAmount'].fillna(trainData["LoanAmount"].median(), inplace=True)
testData['LoanAmount'].fillna(testData["LoanAmount"].median(), inplace=True)

trainData['Loan_Amount_Term'].fillna(trainData["Loan_Amount_Term"].median(), inplace=True)
testData['Loan_Amount_Term'].fillna(testData["Loan_Amount_Term"].median(), inplace=True)

trainData['Credit_History'].fillna(trainData["Credit_History"].median(), inplace=True)
testData['Credit_History'].fillna(testData["Credit_History"].median(), inplace=True)


from sklearn.preprocessing import LabelEncoder

labelEnc=LabelEncoder()

cat_vars=['Gender','Married','Dependents', 'Education', 'Self_Employed','Property_Area']

for col in cat_vars:
    trainData[col]=labelEnc.fit_transform(trainData[col].astype('str'))
    testData[col]=labelEnc.fit_transform(testData[col].astype('str'))

trainData['Gender'].fillna(trainData["Gender"].median(), inplace=True)
testData['Gender'].fillna(testData["Gender"].median(), inplace=True)
    
print(trainData.isnull().sum())
print(testData.isnull().sum())
print(len(trainData.columns)-1)



X = trainData.iloc[:,0:10]
Y = trainData['Loan_Status']
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

validation_size = 0.20
seed = 6
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

scoring = 'accuracy'
#Algos are binary classfier
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
print(X_validation.columns) 
#LDA is giving better result
clf = LinearDiscriminantAnalysis()
clf.fit(X_train, Y_train)
test_id = testData['Application_ID']
preds = clf.predict(testData[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History']])

print(len(preds))
out_df = pd.DataFrame({"Application_ID":test_id, "Loan_Status":preds})
print(out_df[200:250])
file = out_df.to_csv("techgig_submission.csv", index=False)

