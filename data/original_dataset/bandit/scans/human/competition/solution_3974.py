m,p,c=0,0,0
s=(input())
for i in  s:
    if i=='-':
        c-=1
    else:
        c+=1    
    m=min(m,c)
    p=max(p,c)
print(p-m)