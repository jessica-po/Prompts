n = int(input())
a = []
a = input().split()
a = [int(i) for i in a]
a.sort()
ans = 0
for i in range(n // 2):
    ans += (a[i] + a[n - i - 1]) ** 2
print(ans)