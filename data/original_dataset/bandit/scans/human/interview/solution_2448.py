t = int(input())

for _ in range(t):
	n = int(input())
	a, b, c = map(int, input().split())
	s = input()

	t = ["X"] * n
	wins = 0
	for i, en in enumerate(s):
		if en=="R" and b:
			b-=1
			t[i] = "P"
			wins += 1
		elif en=="P" and c:
			c-=1
			t[i] = "S"
			wins += 1
		elif en=="S" and a:
			a-=1
			t[i] = "R"
			wins += 1

	if wins < n/2:
		print("NO")
	else:
		print("YES")
		for i, my in enumerate(t):
			if my=="X":
				if a:a-=1;t[i]="R"
				elif b:b-=1;t[i]="P"
				elif c:c-=1;t[i]="S"
		print("".join(t))