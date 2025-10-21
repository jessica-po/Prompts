import sys
input = sys.stdin.readline
n, M = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = []
tmp = [0] * 101
for i in range(n):
    num = 0
    T = t[i]
    for j in range(1, 101):
        if T + j * tmp[j] <= M:
            num += tmp[j]
            T += j * tmp[j]
        else:
            m = M - T
            num += m // j
            break

    ans.append(i - num)
    tmp[t[i]] += 1

print(*ans)