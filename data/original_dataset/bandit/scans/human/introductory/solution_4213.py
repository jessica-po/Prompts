# coding: utf-8
# Your code here!
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans=max(abs(a[i]-a[j]),ans)
print(ans)