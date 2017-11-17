# -*- coding: utf-8 -*-
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
#from pandas.tools.plotting import scatter_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import sklearn.metrics as mt
import numpy as np 
import pandas as pd 
testfile = "input/test_data.csv"
trainfile = "input/train_data.csv"
trainData = pd.read_csv(trainfile,sep=",")
testData = pd.read_csv(testfile,sep=",")
print(trainData.columns)
#print(trainData.groupby('Loan_Status').size())
#print(trainData.info())

trainData = trainData.drop(['Application_ID'],axis=1)
trainData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'] = trainData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'].fillna('M')
testData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'] = testData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'].fillna('M')
testData.ix[testData['ApplicantIncome']<testData['CoapplicantIncome'],'Gender'] = testData.ix[testData['ApplicantIncome']<testData['CoapplicantIncome'],'Gender'].fillna('F')

testData.ix[testData['CoapplicantIncome']>0,'Married'] = testData.ix[testData['CoapplicantIncome']>0,'Married'].fillna('Yes')
testData.ix[testData['CoapplicantIncome'] ==0,'Married'] = testData.ix[testData['CoapplicantIncome'] ==0,'Married'].fillna('No')

testData.ix[testData['CoapplicantIncome']>0,'Dependents'] = testData.ix[testData['CoapplicantIncome']>0,'Dependents'].fillna(1)
testData.ix[testData['CoapplicantIncome'] ==0,'Dependents'] = testData.ix[testData['CoapplicantIncome'] ==0,'Dependents'].fillna(0)

trainData['Self_Employed'].fillna('No', inplace=True)
testData['Self_Employed'].fillna('No', inplace=True)

trainData['Credit_History'].fillna(2.0, inplace=True)
testData['Credit_History'].fillna(2.0, inplace=True)

mean = np.mean(trainData['LoanAmount'], axis=0)
sd = np.std(trainData['LoanAmount'], axis=0)
l = mean - 2 * sd
h = mean + 2 * sd
t = trainData['LoanAmount'][trainData['LoanAmount'] > l][trainData['LoanAmount'] < h]
#print(t.mean())
trainData['LoanAmount'].fillna(t.mean(), inplace=True)
testData['LoanAmount'].fillna(t.mean(), inplace=True)

trainData['Loan_Amount_Term'].fillna(360, inplace=True)
testData['Loan_Amount_Term'].fillna(360, inplace=True)
#null_columns=trainData.columns[trainData.isnull().any()]
#print(null_columns)
#print(trainData.isnull().sum())
#print(testData.isnull().sum())                      
#trainData.hist(figsize=(10,10))

from sklearn.preprocessing import LabelEncoder

labelEnc=LabelEncoder()

cat_vars=['Property_Area','Dependents','Gender','Married','Education','Self_Employed']

for col in cat_vars:
    trainData[col]=labelEnc.fit_transform(trainData[col].astype('str'))
    testData[col]=labelEnc.fit_transform(testData[col].astype('str'))

##new features
#trainData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'] = trainData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'].fillna('M')
#testData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'] = testData.ix[testData['ApplicantIncome']>testData['CoapplicantIncome'],'Gender'].fillna('M')

d = []
for i, j, k in zip(trainData['Dependents'],trainData['Married'],trainData['CoapplicantIncome']):
    if(j==1 and k>0):
#        print('Yes')
        d.append(i+2)
    else:
        d.append(i+1)
    
trainData['familySize'] = d
d = []
for i, j, k in zip(testData['Dependents'],testData['Married'],testData['CoapplicantIncome']):
    if(j==1 and k>0):
#        print('Yes')
        d.append(i+2)
    else:
        d.append(i+1)

testData['familySize'] = d

trainData['totalIncome'] = trainData['ApplicantIncome'] +trainData['CoapplicantIncome']
testData['totalIncome'] = testData['ApplicantIncome'] +testData['CoapplicantIncome']

trainData['ipc'] = trainData['totalIncome']/(trainData['familySize'])
testData['ipc'] = testData['totalIncome']/(testData['familySize'])

trainData['emi'] = trainData['LoanAmount']/trainData['Loan_Amount_Term']
testData['emi'] = testData['LoanAmount']/testData['Loan_Amount_Term']

trainData['ltoI'] = trainData['emi']/(trainData['totalIncome'])
testData['ltoI'] = testData['emi']/(testData['totalIncome'])
    
trainData['emipc'] = trainData['emi']/trainData['ipc']
testData['emipc'] = testData['emi']/testData['ipc']


for i in ['ApplicantIncome','LoanAmount','totalIncome','ipc','ltoI','emi','emipc']:
    trainData['Log_'+i]=np.log(trainData[i]*100000)
    testData['Log_'+i]=np.log(testData[i]*100000)
#
print(trainData.groupby('familySize').size())    
print(testData.groupby('familySize').size())    

    
    
X = trainData[trainData.drop(['Loan_Status'],axis=1).columns]

Y = trainData['Loan_Status']

#print(X.corr())
select_top = SelectKBest(score_func=chi2, k = 15)
fit = select_top.fit(X,Y)
features = fit.transform(X)
T = fit.transform(testData[X.columns])
idxs_selected = select_top.get_support(indices=True)
print(idxs_selected)
# Create new dataframe with only desired columns, or overwrite existing
X = X[idxs_selected]
#
from sklearn.preprocessing import StandardScaler
rescaledX = StandardScaler().fit_transform(features)
rescaledt = StandardScaler().fit_transform(T)
X = pd.DataFrame(data = rescaledX, columns= X.columns)
t = pd.DataFrame(data = rescaledt, columns= X.columns)
print(trainData.columns)

#print(X.head())
validation_size = 0.40
seed = 4
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier(min_samples_split=4,max_depth=12)))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC()))
results = []
names = []
#
for name, model in models:
    kfold = model_selection.KFold(n_splits=7, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    s = model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)
    results.append(cv_results)
    accuracy = mt.accuracy_score(predictions,Y_validation)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg,"Accuracy : %s" % "{0:.3%}".format(accuracy),s.score(X_train, Y_train))
    test_id = testData['Application_ID']

    preds = model.predict(t[X_validation.columns])
    out_df = pd.DataFrame({"Application_ID":test_id, "Loan_Status":preds})
    print(out_df.groupby('Loan_Status').size())
    print(mt.confusion_matrix(predictions,Y_validation))
    file = out_df.to_csv("techgig_"+name+"_submission.csv", index=False)
clf = RandomForestClassifier(
#                             n_estimators=50
#                             , min_samples_split=2
#                             ,max_depth=85
#,max_features=9
 )
cv_results = model_selection.cross_val_score(clf, X_train, Y_train, cv=kfold, scoring=scoring)
   
s = clf.fit(X_train, Y_train)
predictions = clf.predict(X_validation)
results.append(cv_results)
accuracy = mt.accuracy_score(predictions,Y_validation)
msg = "%s: %f (%f)" % ("RFC", cv_results.mean(), cv_results.std())
print(msg,"Accuracy : %s" % "{0:.3%}".format(accuracy),s.score(X_train, Y_train))
test_id = testData['Application_ID']

preds = clf.predict(t[X_validation.columns])
out_df = pd.DataFrame({"Application_ID":test_id, "Loan_Status":preds})
print(out_df.groupby('Loan_Status').size())
print(mt.confusion_matrix(predictions,Y_validation))

#featimp = pd.Series(clf.feature_importances_).sort_values(ascending=False)
#print(X.columns[featimp.index])
file = out_df.to_csv("techgig_rfc_submission.csv", index=False)