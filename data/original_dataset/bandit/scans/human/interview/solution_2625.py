t = int(input())

for case in range(0,t):
	x, n = map(int, input().split())
	print(n+(x-1)*9)