def main():
	N = int(input())
	L = [int(l) for l in input().split(" ")]
	L.sort()
	m = len(L)
	cnt = 0
	for i in range(m):
		k = m - 1
		for j in range(i + 1, m):
			while m + i - j < k:
				if L[m + i - j] + L[i] <= L[k]:
					k -= 1
				else:
					cnt += k - m - i + j
					break
	print(cnt)

main()