# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:08:10 2015

@author: Ratnesh Kushwaha
"""

import numpy as np
X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]]) 
Y=np.array([1,1,1,2,2,2])
from sklearn.naive_bayes import GaussianNB
clf =GaussianNB()
clf.fit(X,Y)
print(clf.predict([[-0.1,0],[-0.1,0]]))

from sklearn.metrics import accuracy_score
#print accuracy_score()