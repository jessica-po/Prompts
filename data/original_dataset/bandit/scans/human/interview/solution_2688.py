n=int(input())
arr=[0]+[int(x) for x in input().split()]
used=[]
ans=[]
for i in range (1,n+1) :
    d=[]
    start,end=i,arr[i]
    if i not in used :
       d.append(i)
       used.append(i)
       while(True) :
        d.append(end)
        if end==start :
            break
        else :
            used.append(end)
            end=arr[end]
    if len(d)>0 :
        ans.append(d)
print(len(ans))
for i in ans :
    print(*i)