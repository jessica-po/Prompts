ar=[]
for i in range(1,10**5):
    if(i*i>2*10**9):break
    ar.append(i*i)
s=input()
ans=len(s)
for x in ar:
    s2=str(x)
    i=0
    for x in range(len(s)):
        if i<len(s2) and s[x]==s2[i]:
            i+=1
    if(i==len(s2)):
        ans=min(ans,len(s)-i)
if(ans==len(s)):
    print(-1)
else:
    print(ans)