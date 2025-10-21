n = int(input())
a = [int(x) for x in input().split()]
b = [(a[i], i + 1) for i in range(n)]
b.sort(reverse=True)
ans = 0
for i in range(n):
    ans += b[i][0] * i + 1
print(ans)
for i in b:
    print(i[1], end=' ')