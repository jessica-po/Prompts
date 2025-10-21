def solve(a, e):
	if not a[e]:
		return False, []
	a = list(a[::])
	ans = [e]
	a[e] -= 1
	for i in range(sum(a)):
		if ans[-1] - 1 >= 0 and a[ans[-1] - 1] > 0:
			v = ans[-1] - 1
			ans.append(v)
			a[v] -= 1
		elif ans[-1] + 1 <= 3 and a[ans[-1] + 1] > 0:
			v = ans[-1] + 1
			ans.append(v)
			a[v] -= 1
		else:
			return False, []
	return True, ans

def main():
	a = list(map(int, input().split()))
	for i in range(4):
		r, b = solve(a, i)
		if r:
			print('YES')
			print(*b)
			return
	print('NO')

main()