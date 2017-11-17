# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
 
# Create data
#N = 60
#g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N),0.4+0.1*np.random.rand(N))
#g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N),0.1*np.random.rand(N))
#g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N),0.3*np.random.rand(N))
file ="input/all.csv"
df=pd.read_csv(file,sep=",")
#print(df.columns)  
ph = df[df['State']=='ArunachalPradesh']['ST.1.Population'].astype(int)
sph = df[df['State']=='ArunachalPradesh']['ST.2.Population'].astype(int)
th=df[df['State']=='ArunachalPradesh']['ST.3.Population'].astype(int)
ph1 = df[df['State']=='Assam']['ST.1.Population'].astype(int)
sph1 = df[df['State']=='Assam']['ST.2.Population'].astype(int)
th1=df[df['State']=='Assam']['ST.3.Population'].astype(int)
ph2 = df[df['State']=='Bihar']['ST.1.Population'].astype(int)
sph2 = df[df['State']=='Bihar']['ST.2.Population'].astype(int)
th2=df[df['State']=='Bihar']['ST.3.Population'].astype(int)
#
g1 = (ph, sph, th)
g2 = (ph1, sph1, th1)
g3 = (ph2, sph2, th2)
##g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N),0.1*np.random.rand(N))
##g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N),0.3*np.random.rand(N))
    
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("AP", "A", "B")
markers = ("o","^","*")
#print(data.info())
#print(type(g2))
#print(g1[1][0])
#print(g2[1][0])
#print(g3[1][0])

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
ax = fig.gca(projection='3d')
 
for data, color, group, m in zip(data, colors, groups,markers):
    x, y, z = data
    
    ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors=color,marker =m, s=30, label=group)

#x, y, z = g2
##    print(x)
#print(y[0])
##    print(z)
#ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Matplot 3d scatter plot')
plt.legend(loc=2)
plt.show()


#def randrange(n, vmin, vmax):
#    '''
#    Helper function to make an array of random numbers having shape (n, )
#    with each number distributed Uniform(vmin, vmax).
#    '''
#    return (vmax - vmin)*np.random.rand(n) + vmin
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
#n = 100
#
## For each set of style and range settings, plot n random points in the box
## defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
#for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#    xs = ph
#    ys = sph
#    zs = th
#    ax.scatter(xs, ys, zs, c=c, marker=m)
z#
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
#
#plt.show()