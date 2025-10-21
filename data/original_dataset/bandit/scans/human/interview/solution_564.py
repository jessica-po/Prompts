n,s=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
if sum(a[:-1])<=s:
    print('YES')
else:
    print('NO')