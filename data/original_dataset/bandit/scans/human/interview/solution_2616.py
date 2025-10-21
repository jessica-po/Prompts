from math import *
from collections import *
from random import *
from bisect import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    z=a.count(1)
    if(z==n):
        if(z%2):
            print("First")
        else:
            print("Second")
    else:
        tu=0
        for i in a:
            if(i!=1):
                break
            else:
                tu+=1
        if(tu%2):
            print("Second")
        else:
            print("First")