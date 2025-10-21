import sys, math
n=int(input())
s=input()
z=list(map(int,input().split()))
best = 10**9
for i in range(len(s)-1):
    if s[i]=='R' and s[i+1]=='L':
        best=min(best, z[i+1]-(z[i]+z[i+1])//2)
if best != 10**9:
    print(best)
else:
    print(-1)