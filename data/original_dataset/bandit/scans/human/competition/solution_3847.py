import bisect
n,m=list(map(int,input().split()))
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
x=int(input())
newL1=[0]
newL2=[0]
for i in L1:newL1.append(newL1[-1]+i)
for i in L2:newL2.append(newL2[-1]+i)
min1=[]
min2=[]
mx=9999999999999999999
for i in range(1,n+1):
    m1=mx
    for j in range(n-i+1):
        if newL1[j+i]-newL1[j]<m1:m1=newL1[j+i]-newL1[j]
    min1.append(m1)
for i in range(1,m+1):
    m2=mx
    for j in range(m-i+1):
        if newL2[j+i]-newL2[j]<m2:m2=newL2[j+i]-newL2[j]
    min2.append(m2)
area=0
for i in range(n):
    k=x//min1[i]
    for j in range(m):
        if min2[j]>k:break
    if min2[-1]<=k:j+=1
    if area<j*(i+1):area=j*(i+1)
print(area)