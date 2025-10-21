t = int(input())
for _ in range(t):
	s = input()
	n = len(s)
	if s.count('1') == n or s.count('1') == 0:
		print(s)
	else:
		odp = [0,1]*n
		for i in range(n):
			if i < n-1:
				print("01", end = "")
			else:
				print("01")