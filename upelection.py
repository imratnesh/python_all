# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "input/up_res.csv"
data = pd.read_csv(file,sep=",")

#print(data.head())
#print(data.info())
#print(data.shape)
datax = data[['candidate','party','phase','votes']][data['party'] !='None of the Above'][data['party'] !='others']
cand_names = datax['candidate']
def surnames(x):
    return x.split()[-1]

#print(cand_names[0:5])
#print(cand_names[0].split()[-1])
datax['surname'] = cand_names.map(surnames)

#print(data[['party','surname']][5:10])
#print(data.groupby('surname').size())
surnames =datax['surname']
surnames.value_counts()[0:20].plot("bar")

top10_caste = surnames.value_counts()[0:10].index
print(top10_caste)
#l=[]
#for c in top10_caste:
#    caste_per_party = datax[datax['surname']==c].groupby('party').size()
#    l.append(caste_per_party.values)
#    
#l = pd.DataFrame(l)    
s=datax.groupby('party')['surname'].value_counts()
print(s['BJP+'][0:5])

l=[]
for p in ['BJP+', 'BSP', 'INC', 'Independent', 'RLD', 'SP']:
    caste_per_party = s[p][top10_caste]
    l.append(caste_per_party.values)
    print(caste_per_party)

#print(l.fillna(0))
df = pd.DataFrame(l,index=['BJP+', 'BSP', 'INC', 'Independent', 'RLD', 'SP'],columns=top10_caste)
df.plot(kind="bar",stacked=True)

s=datax.groupby('phase')['surname'].value_counts()
#print(s['BJP+'][0:5])

l=[]
for p in range(1,8):
    caste_per_party = s[p][top10_caste]
    l.append(caste_per_party.values)
    print(caste_per_party)

#print(l.fillna(0))
df = pd.DataFrame(l,index=range(1,8),columns=top10_caste)
df.plot(kind="bar",stacked=True)

#s=datax.groupby('phase')['surname'].value_counts()
#
#print(s[1].head())

#print(data.groupby('phase').size())
#print(data.groupby('phase').size())

#data['phase'].value_counts().plot("bar")
#party_col.value_counts().plot("pie")
#data.describe()

#s = data.groupby('ac_no')['votes'].max()
#win = []
#for val in zip(s.values,s.index):
## if(data[data['votes']== val]['party'] == "INC"):
##  if(len(data[data['votes']== val]['party'].values)>1):
##      print(data[data['votes']== val])
##  if((data[data['votes']== val]['party'].values.any("None of the Above"))):
##      print(s)
# win.append(data[data['votes']==val[0]][data['ac_no']==val[1]])
#s = data.groupby('ac_no')['votes'].max()
#print(len(s))
#wins = data[(data['votes'].isin(s))]
#print (wins)
#party_col=data['party']
#
#seats_per_party =party_col.value_counts()
#print(seats_per_party.index)
#print(seats_per_party.values)
#l = []
#for v in range(1,8):
#    votes_vs_party= data[data['phase']==v].groupby('party')['votes'].sum()
#    votes_per_party = np.array([votes_vs_party.values])
#    l.append(votes_vs_party.values)
#    l.extend([votes_vs_party.values])
#    print(votes_vs_party.values)
    
#votes_percentage_party = votes_per_party/votes_per_party.sum()*100

#print(votes_percentage_party)
#print(np.array(votes_vs_party.keys))

#district= data.groupby('district')['votes'].sum()
#sd=sorted(district,reverse=True)
#for i in sd[0:5]:
#    print(district[district == i])

#for i in sd[-5:]:
#    print(district[district == i])

#plt.figure(figsize=(8,8))
#plt.pie(votes_per_party,labels=sorted(set(party_col)),shadow=True)
#plt.show()

#print(np.where(data['votes']==44))
#print(data.iloc[177])
#l = np.random.rand(7, 8)
#l = np.array(l)
#print(type(l))
##print(l)
#print(l.shape)
#
#data2 = pd.DataFrame(l, columns= votes_vs_party.index, index=range(1,8))
#data2.plot.barh(figsize=(10,10),stacked=True)
