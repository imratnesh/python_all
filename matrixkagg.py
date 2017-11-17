# -*- coding: utf-8 -*-
import numpy as np
def main():
  row = int(input())
#  col = int(input())
##  array = input()    
#  a = []  
#  for i in range(row):
#          a.append(input().split(' '))
#  
#  matrix = [a]  
  matrix = [['0','3','1','2'],['0','1','0','3'],['1','2','3','0'],['1','2','8','9']]  
#          
#  print(matrix)   
#  print(matrix[0:2,0:2])
#  print(matrix[2:4,0:2])
#  print(matrix[0:2,2:4])
#  print(matrix[2:4,2:4])
  magic_square = True
  s = set([str(i) for i in range(row)])
  
  for i in range(int(row/2)):
      for j in range(int(row/2)):
           mat = set(matrix[i*2:i*2+2,j*2:j*2+2].reshape(-1))
           if(len(s.intersection(mat))!=row):
               magic_square = False
               print(False)
           
  for r in matrix:
      if(len(s.intersection(r))!=row):
           magic_square = False
           print(False,'--')
               
  for r in np.matrix.transpose(matrix):
      print(r)
      if(len(s.intersection(r))!=row):
           magic_square = False
           print(False,'--')
               
  print(magic_square)     
     
          
main()