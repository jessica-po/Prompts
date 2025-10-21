t = int(input())
for tc in range(t):
    n,k=list(map(int, input().split()))
    tap = list(map(int, input().split()))
    sol=0
    for i in range(1, n+1):
        d=1000000
        for j in tap:
            d=min(d, abs(j-i)+1)
        sol=max(sol, d)
    print(sol)