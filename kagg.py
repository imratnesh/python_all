# -*- coding: utf-8 -*-
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import numpy as np    
import pandas as pd
#import h5py as hf
def main():
# nums = input().split(' ')
# num = []
# for n in nums:
#     if(n != ''):
#         num.append(int(n))
# num1 = num[0]        
# num2 = num[1]        
# print(num1,num2)        
# num1sum = 0
# num2sum = 0
# while(num1 >0):
#     digit = num1%10
#     num1sum = num1sum +digit
#     num1 = int(num1/10)
# while(num2 >0):
#     digit = num2%10
#     num2sum = num2sum +digit
#     num2 = int(num2/10)
#     
# if(num1sum==num2sum):
#     print('Equal')
# if(num1sum>num2sum):
#     print(int(num[0]))
# if(num1sum<num2sum):
#     print(int(num[1]))
# print(hf.key())
 df = pd.DataFrame({'Id':[1,2,3,4],'val':[2,5,np.nan,6]})
 print(df.val == np.nan)
 D = ['A','B','C','D','E','AA','AB']
 from sklearn.preprocessing import LabelEncoder
 le = LabelEncoder()
 print(le.fit_transform(D))
 tup = (1,2,3,4,5)
 print(tup[2])
 g = [10,11,12]
 print(fun(g),g)
def fun(x):
    x[0] = 5
    return x
# train  = pd.DataFrame({'id':[1,2,4],'features':[["A","B","C"],["A","D","E"],["C","D","F"]]})
#
# train['features_t'] = train["features"].apply(lambda x: " ".join(["_".join(i.split(" ")) for i in x]))
#
# print(train['features_t'])
#
# nums = input().split(' ')
# num = []
# for n in nums:
#     if(n != ''):
#         num.append(int(n))
# r = num[0]        
# c = num[1]
# rows = []        
## diag1 =0
## diag2 =0
# for i in range(r):
#     rows.append(input("row").split(' '))
# sums = []    
# for i in range(r):
#     rowsum =0
#     for j in range(c):
#       rowsum +=  int(rows[i][j])
#     sums.append(rowsum)
#             
# print('Row ', sums.index(max(sums))+1)    
# for i in range(num1):
#     for j in range(num2):
#         if(i==j):
#             diag1 += int(rows[i][j])
#         if((i+j)==(num1-1)):
#             diag2 += int(rows[i][j])

# if(diag1==diag2):
#     print('Equal')
# if(diag1>diag2):
#     print('Diagonal 1')
# if(diag1<diag2):
#     print('Diagonal 2')             
main()

#if((digit & 1)==0):
#         even = even+digit
#     else:    
#         odd = odd+digit
#     num=int(num/10)
#     
# max_num = max(even,odd) 
# min_num = min(even,odd) 
     