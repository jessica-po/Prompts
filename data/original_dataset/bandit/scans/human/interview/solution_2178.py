n = int(input())
a = list(map(int, input().split()))[::-1]
b = list(map(int, input().split()))
ans = [0] * n
marked = [True] * (n + 1)
for i in range(n):
    if marked[b[i]]:
        while True:
            marked[a[-1]] = False
            ans[i] += 1
            if a[-1] == b[i]:
                a.pop()
                break
            a.pop()
    else:
        continue
print(*ans)