# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:41:20 2015

@author: Ratnesh Kushwaha
"""

#%%writefile ClassifyNB.py

from sklearn.naive_bayes  import GaussianNB
from sklearn.svm import SVC
from sklearn import tree
def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    clf = GaussianNB()
    clf.fit(features_train,labels_train)
    return clf
    
### import the sklearn module for GaussianNB
    
def classifySVM(features_train, labels_train):
    ### create classifier
    clf = SVC(kernel= 'rbf', gamma=100.0, C=1000.0)
    clf.fit(features_train,labels_train)
    return clf
    
def classifyTree(features_train, labels_train):
    ### create classifier
    clf = tree.DecisionTreeClassifier(min_samples_split=0)
    clf.fit(features_train,labels_train)
    return clf