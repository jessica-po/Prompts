# cook your dish here
n=int(input())
count=[]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
start=0
for i in range(n):
    if a[i]>=start:
        count.append(i)
        start=b[i]
print(*count,sep=" ")