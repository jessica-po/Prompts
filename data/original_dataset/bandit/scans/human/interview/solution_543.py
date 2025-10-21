n=input()
c=[int(x) for x in input().split()]
p=0
d=True
for i in c:
    #print(p,d,i)
    if i%2==0:
        if p==1:
            if i==0:
                d=False
    else:
        p=1-p

print('YES' if d and p==0 else 'NO')