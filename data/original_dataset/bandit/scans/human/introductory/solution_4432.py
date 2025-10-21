for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    lis=[]
    prevsign=-1
    if l[0]>0:
        prevsign=1
    else:
        prevsign=0
    i=0
    for i in l:
        if (i>0 and prevsign==1) or (i<0 and prevsign==0):
            lis.append(i)
        else:
            if prevsign==1:
                a.append(max(lis))
                lis=[]
                lis.append(i)
                prevsign=0
            else:
                a.append(max(lis))
                lis=[]
                lis.append(i)
                prevsign=1
    
    if prevsign==1:
        a.append(max(lis))
        lis=[]
        lis.append(i)
        prevsign=0
    else:
        a.append(max(lis))
        lis=[]
        lis.append(i)
        prevsign=1
    print(sum(a))