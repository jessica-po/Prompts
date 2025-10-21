n = int(input())
a = list(map(int, input().split()))
a.sort()
ok = False
for i in range(n - 2):
	if a[i] + a[i + 1] > a[i + 2]:
		ok = True
print(("NO", "YES")[ok])