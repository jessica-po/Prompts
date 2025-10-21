3

def readln(): return tuple(map(int, input().split()))

n, m = readln()
cnt = [0] * (m + 1)
for c in readln():
    cnt[c] += 1
ans = [0] * n
j = 0
for _ in range(1, m + 1):
    v = max(cnt)
    i = cnt.index(v)
    while cnt[i]:
        ans[j] = i
        cnt[i] -= 1
        j += 2
        if j >= n:
            j = 1
print(len([1 for i in range(n) if ans[i] != ans[(i + 1) % n]]))
for i in range(n):
    print(ans[i], ans[(i + 1) % n])