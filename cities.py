# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# Any results you write to the current directory are saved as output.
file = "input/emergent.csv"
data = pd.read_csv(file,sep=',')
claim_label = data['claim_label']
df = pd.DataFrame({'a':claim_label})
#cnt =df.a.value_counts()
#print(cnt)
#plt.bar(cnt.index,cnt.values,width=1.0)
#data['claim_label'].value_counts().plot(kind='bar')  
print(type(data['claim_label']))
plt.xlabel("Claim labels")
plt.ylabel("Counts")
plt.title("Claim labels count in Emergent")

#plt.savefig('fig.png')
#plt.show()
df = pd.DataFrame(data)
df.iloc[:,1].value_counts().plot(kind='bar',figsize=(10,10))

print(df.iloc[:,4])

