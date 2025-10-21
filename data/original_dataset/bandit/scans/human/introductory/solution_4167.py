n,k = map(int,input().split())

cnt1,cnt2 = 0,0
if k%2 == 1:
    for i in range(1,n+1):
        if i%k == 0:
            cnt1 +=1
    print(cnt1**3)
else:
    for i in range(1,n+1):
        if  i%k == k//2:
            cnt2 += 1
    for i in range(1,n+1):
        if i%k == 0:
            cnt1 +=1
    print(cnt1**3+cnt2**3)