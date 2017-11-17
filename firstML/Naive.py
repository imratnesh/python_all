# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:17:49 2015

@author: Ratnesh Kushwaha
"""


#Writing prep_terrain_data.py


#Writing class_vis.py


#Overwriting ClassifyNB.py

# %%writefile GaussianNB_Deployment_on_Terrain_Data.py
#!/usr/bin/python

""" Complete the code below with the sklearn Naaive Bayes
    classifier to classify the terrain data

    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify, classifySVM, classifyTree

import numpy as np
import pylab as pl

#from ggplot import *

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#clf = classifyTree(features_train, labels_train)
clf = classifySVM(features_train, labels_train)

    ### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())



#Overwriting classify.py

# %%writefile submitAccuracy.py
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy
from classify import SVMAccuracy
from classify import TreeAccuracy


import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy


def submitSvmAccuracy():
    accuracy = SVMAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy

def submitTreeAccuracy():
    accuracy = TreeAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy

print("Naive ") 
print(submitAccuracy())
print( 'SVM ' )
print(submitSvmAccuracy())
print('Tree ')
print(submitTreeAccuracy())
