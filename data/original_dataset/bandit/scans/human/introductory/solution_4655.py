from sys import stdin,stdout
import sys
import math

t=int(stdin.readline())
for i in range(t):
    a=list(map(int,stdin.readline().split()))
    print(sum(a)//2)