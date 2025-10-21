t=int(input())
for i in range(t):
    n,s,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s=s-1
    for i in range(n):
        if (s-i)>-1:
            if not (s-i+1) in a:
                print(i)
                break
        if (s+i)<n:
            if not (s+i+1) in a:
                print(i)
                break