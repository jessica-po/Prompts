n, m, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
	orders = map(int, input().split())
	for order in orders:
		ans += a.index(order) + 1
		a.remove(order)
		a.insert(0, order)
print(ans)