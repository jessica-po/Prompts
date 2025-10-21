n=int(input())
a=list(map(int,input().split()))
a.sort()
prev=-2
c=0
for i in a:
    dif=i-prev
    if dif > 1:
        prev=i+1
        c+=1
ac=0
lc=-2
for i in a:
    if lc < i-1:
        lc=i-1
        ac+=1
    elif lc == i-1:
        lc=i
        ac+=1
    elif lc == i:
        lc=i+1
        ac+=1
print(c,ac)