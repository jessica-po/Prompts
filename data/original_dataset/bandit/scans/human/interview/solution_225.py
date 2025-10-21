l=list(map(int,input().split()))
for i in range(16):
    cur1,cur2=0,0
    for j in range(4):
        if (i&(1<<j))==0:
            cur1+=l[j]
        else:
            cur2+=l[j]
    if cur1==cur2:
        print("YES")
        quit()
print("NO")