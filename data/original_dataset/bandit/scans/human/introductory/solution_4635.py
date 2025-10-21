n = int(input())
for i in range(n):
	l, ch = map(int, input().split())
	for j in range(l):
		print(chr(j % ch + ord('a')), end='')
	print()