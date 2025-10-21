n, v = map(int, input().split())
ans = []
for i in range(n):
    a = list(map(int, input().split()))[1:]
    if v > min(a):
        ans.append(i + 1)
print(len(ans))
print(*ans)