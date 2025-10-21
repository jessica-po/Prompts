N,A,B,C = map(int,input().split())
l = [int(input()) for _ in range(N)]
ans = float("inf")
for i in range(4**N):
    a,b,c = [],[],[]
    cost = 0
    for j in range(N):
        r = (i//(4**j)) % 4
        if r == 1:
            a.append(l[j])
        elif r == 2:
            b.append(l[j])
        elif r == 3:
            c.append(l[j])
    if a and b and c:
        cost += sum(max((len(x)-1), 0)*10 for x in [a,b,c])
        a = sum(a)
        b = sum(b)
        c = sum(c)
        cost += sum(abs(x-y) for x,y in [(a,A),(b,B),(c,C)])
        ans = min(ans, cost)
print(ans)