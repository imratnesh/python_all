# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:09:17 2015

@author: Ratnesh Kushwaha
"""
from sklearn import svm
X =[[0,0],[1,1]]
Y=[0,1]
clf = svm.SVC()
clf.fit(X,Y)
print (clf.predict([2.,2.]))

from sklearn.metrics import accuracy_score
print (accuracy_score())