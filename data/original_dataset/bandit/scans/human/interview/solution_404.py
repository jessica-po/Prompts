#JMD
#Nagendra Jha-4096

 
import sys
import math

#import fractions
#import numpy
 
###File Operations###
fileoperation=0
if(fileoperation):
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    inputfile = open('W:/Competitive Programming/input.txt', 'r')
    outputfile = open('W:/Competitive Programming/output.txt', 'w')
    sys.stdin = inputfile
    sys.stdout = outputfile

###Defines...###
mod=1000000007
 
###FUF's...###
def nospace(l):
    ans=''.join(str(i) for i in l)
    return ans

ans=[]

def printDivisors(n) : 
      
    # Note that this loop runs till square root 
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                ans.append(i) 
            else : 
                # Otherwise print both 
                ans.append(i)
                ans.append(n//i) 
        i = i + 1
 
 
 
##### Main ####
t=1
for tt in range(t):
	n=int(input())
	printDivisors(n)
	s=set(ans)
	print(len(s))
    #a=list(map(int,sys.stdin.readline().split(' ')))
    #n,k,s= map(int, sys.stdin.readline().split(' '))
    
    
#####File Operations#####
if(fileoperation):
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    inputfile.close()
    outputfile.close()