# -*- coding: utf-8 -*-
input1 = ['12#45#33','94#54#23','98#59#27']
n= len(input1)
a = [[0] * n for i in range(n)]
i=-1
for r in input1:
    row = r.split('#')
    i=i+1
    for j in range(len(row)):
#            print(row[j])
            a[i][j] = row[j]
print(a)            
        
for i in range(len(row)):
    for j in range(len(row)):
        if(i==0 and j==0):
            print("1.",i,j)
            print(i,j,'#',i,j+1,'#',i+1,j,'#',i+1,j+1)
        elif(j==(len(row)-1) and i==(len(row)-1)):
            print("6.",i,j)
            print(i-1,j-1,'#',i-1,j,'#',
                  i,j-1,'#',i,j)
        elif(i==0 and j!=(len(row)-1)):
            print("2.",i,j)
            print(i,j-1,'#',i,j,'#',i,j+1,'#',
                  i+1,j-1,'#',i+1,j,'#',i+1,j+1)
        elif(j==0 and i!=(len(row)-1)):
            print("3.",i,j)
            print(i-1,j,'#',i-1,j+1,'#',i,j,'#',
                  i,j+1,'#',i+1,j-1,'#',
                  i+1,j,'#',i+1,j+1)
        elif(i==0 and j==(len(row)-1)):
            print("4.",i,j)
            print(i,j-1,'#',i,j,'#',
                  i+1,j-1,'#',i+1,j)
        elif(j==0 and i==(len(row)-1)):
            print("5.",i,j)
            print(i-1,j,'#',i-1,j+1,'#',
                  i,j,'#',i,j+1)
        elif(i!=0 and j!=(len(row)-1)):
            print("8.",i,j)
            print(i-1,j-1,'#',i-1,j,'#',i-1,j+1,'#',
                  i,j-1,'#',i,j,'#',i,j+1,'#',
                  i+1,j-1,'#',i+1,j,'#',i+1,j+1)
        elif(j!=0 and i!=(len(row)-1)):
            print("9.",i,j)
            print(i-1,j-1,'#',i-1,j,'#',i-1,j+1,'#',
                  i,j-1,'#',i,j,'#',i,j+1,'#',
                  i+1,j-1,'#',i+1,j,'#',i+1,j+1)
        else:
            print("7.",i,j)
            print(i-1,j-1,'#',i-1,j,'#',i-1,j+1,'#',
                  i,j-1,'#',i,j,'#',i,j+1,'#',
                  i+1,j-1,'#',i+1,j,'#',i+1,j+1)
        