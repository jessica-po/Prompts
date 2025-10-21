n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

temp = 0
ans = 0

for x in a:
    if temp + x < k:
        temp += x
        ans += 1
    else:
        ans = 0

print(ans)