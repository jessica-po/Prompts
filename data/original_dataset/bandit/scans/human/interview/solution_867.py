import sys, math
def rnd(x):
    a = int(x)
    b = x-a
    if b>=0.5:
        a+=1
    return(a)
n = int(input())
print(rnd(n/2))