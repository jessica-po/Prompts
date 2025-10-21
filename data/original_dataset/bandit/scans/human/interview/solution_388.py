n, k = list(map(int, input().split()))
a = input().split()
names = [chr(ord("A") + i) for i in range(26)] + [chr(ord("A") + i) + chr(ord('a') + i) for i in range(26)]
ans = [names[i] for i in range(n)]
for i in range(k - 1, n):
	if a[i - k + 1] == "NO":
		ans[i] = ans[i - k + 1]
print(*ans)