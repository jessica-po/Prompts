from bisect import bisect_left


N, M = list(map(int, input().split()))
S = input()
good = []
bad = []
for i in range(N + 1):
    if S[i] == "1":
        bad.append(i)
    else:
        good.append(i)

ans = []
cur = N
while True:
    if cur == 0:
        print((" ".join(map(str, ans[::-1]))))
        break
    idx = bisect_left(good, cur - M)
    nx = good[idx]
    ans.append(cur - nx)
    if cur == nx:
        print((-1))
        break
    cur = nx