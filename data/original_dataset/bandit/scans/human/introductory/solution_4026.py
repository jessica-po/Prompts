def is_symmetric(a):
	return a[0][1]==a[1][0]
for _ in range(int(input())):
	def two_ints():
		return list(map(int,input().split()))
	n, m = map(int,input().split())
	tiles = [[two_ints(),two_ints()] for i in range(n)]
	print("YES" if m%2==0 and any([is_symmetric(tile) for tile in tiles]) else "NO")