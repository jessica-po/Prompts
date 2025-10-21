########################################################
################# Template #############################
import sys
import math
def Int(): return int(input())
def Str(): return input()
def Ints(): return list(map(int,input().split(" ")))
def int_arr(): return list(map(int,input().strip().split(" ")))
def str_arr(): return list(map(str,input().split(" ")))
def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
#########################################################
#vsInput()
def strings(s):
    n=len(s)
    count=0
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            count=1
            break
    return count==0
    
n=int(input())
s=input()
palindrome = ""
for i in range(n-1):
    for j in range(i+1,n+1):
        nextstring = s[i:j]
        if strings(nextstring) and len(nextstring)>len(palindrome):
            palindrome=nextstring
print(len(palindrome))
print(palindrome)