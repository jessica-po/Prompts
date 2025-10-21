t = int(input())
for i in range(t):
    d,v,l,r = list(map(int, input().split()))
    ans = d // v
    ans -= r//v - (l-1)//v
    print(ans)