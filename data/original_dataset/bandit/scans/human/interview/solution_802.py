from collections import *
c=Counter()
ans=n=int(input())
s=input()
k=len(set(s))
i=j=t=0
while j<n:
    while len(c)<k and j<n: c[s[j]]+=1; j+=1
    while len(c)==k:
        if j-i<ans: ans=j-i
        c[s[i]]-=1
        if c[s[i]]==0: del c[s[i]]
        i+=1
    
print(ans)