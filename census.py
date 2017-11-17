# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file ="input/all.csv"
df=pd.read_csv(file,sep=",")
print(type(df))
plt.figure(figsize=(10,5))
count =df['State'].value_counts()
#count.plot("bar")
person=df['Persons']
education_cols = ['Persons','Below.Primary', 'Primary', 'Middle', 'Matric.Higher.Secondary.Diploma',
                'Graduate.and.Above']
temp = df[education_cols + ['State']].groupby('State').sum()

density =temp.iloc[:,1].values/count.values
print(count + density)

plt.ylabel("Density", size=20)
plt.title("Totals Persons per city in a State", size= 20)
plt.hist(density, color='red')