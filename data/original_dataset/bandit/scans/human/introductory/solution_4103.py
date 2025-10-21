n, b, a = map(int, input().split())
A = list(map(int, input().split()))
a0 = a
ans = 0
for elem in A:
	if a + b == 0:
		break
	if elem == 0:
		if a > 0:
			a -= 1
			ans += 1
		else:
			b -= 1
			ans += 1
	else:
		if a == a0:
			a -= 1
			ans += 1
		elif b > 0:
			b -= 1
			a += 1
			ans += 1
		else:
			a -= 1
			ans += 1
print(ans)