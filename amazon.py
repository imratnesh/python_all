# -*- coding: utf-8 -*-
input4 = ['3 2','2 4','2 5','4 5','1 5']

def main():
  input1 = 5
  input2 = 4
  input3 = [1,2,3]
  possible_paths = list()
  escape_possible = False         
  escape_time = -1
  for i in input4:
      for j in input4:
         vlen = len(set(i).intersection(set(j)))  
         if(vlen!= 1):
             possible_paths.append(set(i).union(set(j)))
           
  s =[ print(i) for i in sorted(possible_paths,key=len)]
  for inp3 in input3:
     for paths in  sorted(possible_paths,key=len):
         if(paths.__contains__(str(inp3)) and paths.__contains__(str(input2))):
             print("Path",paths)
             print("Pair",(inp3,input2))
             print(len(paths)-2)
             escape_time = max(escape_time,len(paths)-2)
             escape_possible =True
             break
         else:
             escape_possible = False  
             
             
  if(escape_possible):           
     print(escape_time)          
  else:         
     print(-1)          
          
#def printPaths(inp3,input2):
#  if(sorted(input4).__contains__([inp3,input2])):
#    possible_paths.append([inp3,input2])
#  
#  if(input4.__contains__([inp3,input2])):
#    possible_paths.append([inp3,input2])
#  
#  return possible_paths
  
main()    
    
