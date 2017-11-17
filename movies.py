# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
#from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
data = "input/movie_metadata.csv"
movie_data = pd.read_csv(data,sep=',')

#print(movie_data.info())
print(movie_data.shape)
#print(movie_data.head(10))
#print(movie_data.describe())

print(movie_data.groupby('imdb_score').size())
#plt.figure(figsize=(40,40))

# box and whisker plots
#movie_data.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False)
#plt.show()

#movie_data.hist(figsize=(20,20))
#plt.show()

# scatter plot matrix
scatter_matrix(movie_data,figsize=(30,30))
plt.show()

movie_data.hist(figsize=(20,20))
