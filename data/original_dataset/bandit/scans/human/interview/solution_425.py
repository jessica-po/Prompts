n, p = list(map(int, input().split()))
for q in range(5757):
    s = bin(n)
    if n >= q >= s.count('1'):
        print(q)
        break
    n -= p
else:
    print(-1)