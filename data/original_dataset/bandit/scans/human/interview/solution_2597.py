n=int(input())
for _ in range(n):
    i=int(input())
    ar=sorted(list(map(int,input().split())))[::-1]
    mx=0
    for e in range(i):
        mx=max(mx,min(e+1,ar[e]))
    print(mx)