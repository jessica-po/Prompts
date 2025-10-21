from math import ceil

N, H = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
else:
    a = max(A)
    B.sort()
    B.reverse()

ans = 0
for b in B:
    if H <= 0:
        print(ans)
        break

    if a < b:
        H -= b
        ans += 1
else:
    print(ans + ceil(H / a))