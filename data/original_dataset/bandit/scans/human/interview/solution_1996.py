n=int(input())
c=set('qwertyuiopasdfghjklzxcvbnm')
ch=False
k=0
for i in range(n-1):
    s=input()
    if ch:
        if s[0]!='.':
            k+=1
    else:
        if s[0]=='.':
            c.difference_update(set(s[2:]))
        elif s[0]=='!':
            c.intersection_update(set(s[2:]))
        else:
            if s[2] in c:
                c.remove(s[2])
        if len(c)==1:
            ch=True
input()
print(k)