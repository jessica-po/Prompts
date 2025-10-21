from math import *
n=int(input())
if n==3:
    li=list(map(int,input().split()))
    ans=0
    flag=0
    for i in li:
        ans^=i
    if ans==0:
        print("BitAryo")
    else:
        print("BitLGM")
elif n==2:
    li=list(map(int,input().split()))
    li.sort()
    phi=(1+sqrt(5))/2
    ch=[0]*(785)
    for i in range(300):
        a=floor(phi*i)
        b=floor((phi**2)*i)
        ch[a]=b
        ch[b]=a
    if ch[li[0]]==li[1]:
        print("BitAryo")
    else:
        print("BitLGM")
else:
    li=int(input())
    if li==0:
        print("BitAryo")
    else:
        print("BitLGM")