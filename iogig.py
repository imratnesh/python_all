''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
    
def main():
#  principal = int(input())
#  rate = int(input())
#  time = int(input())
#  print(rate)
#  simple_interest = principal*rate*time/100
#  print(int(simple_interest))
  
# num = input()
# print(int(num[2])*int(num[6]))
# fact = 1
# for n in range (1,num+1):
#    fact = fact*n
# print(fact)


# start = int(input())
# end = int(input())
# primes = 0
#     
# for n in range(start,end):
#     prime = False
#     for i in range(2,int(n/2)+1):
#         if(n%i == 0):
#             prime = True
#             
#     if(not prime):
#       primes = primes +1
#       
# if(start==1):
#    primes =primes-1      
# print(primes)   
# print(2**3)
# num = input()
# digit_cubes = 0
# for digit in range(0,len(num)):
#    print(int(num[digit])**3)
#    digit_cubes = digit_cubes + int(num[digit])**3
# 
# print(digit_cubes)
# if(digit_cubes == int(num)):
#    print(True)
# else:
#    print(False)   
#    
##    
#    line1 = input()
#    rows = int (line1.split(' ')[0])
#    cols = int (line1.split(' ')[1])
##    print(rows,cols)
#    matrix = [[0 for j in range(cols)] for i in range(rows)]
##    transpose = [[0 for j in range(cols)] for i in range(rows)]
#    
##    print(type(matrix))
#    for r in range(0,rows):
#        row = input()
#        for c in range(cols):
#            matrix[r][c] = int(row.split(' ')[c])
#       
#    for r in range(0,rows):
#        for c in range(cols):
#             print(matrix[c][r]," ",end="")
#        print()     
#    for r in transpose:
#        print()
#    
#    lines = input()
#    base = int (lines.split(' ')[0])
#    exp = int (lines.split(' ')[1])
#    def power(base, exp):
#         if(exp==0):
#             return 1
#         if(exp==1):
#             return base
#         else:    
#             number=base*power(base,exp-1)
#             return number
#             
#    print(power(base,exp))   
        def checkDuplicate(num):  
            numList = []
            while(int(n)>0):
                digit = n%10
                numList.append()
                if(numList.__contains__(digit)):
                   return False
                n=int(n/10)
            return True
    count =0 
    for n in range(1,25):
        if(checkDuplicate(n)):
            count=count+1
        
main()
