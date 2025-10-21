'''input
5
3123 3123
2777 2777
2246 2246
2246 2246
1699 1699
'''
n = int(input())
x = []
f = 0
for _ in range(n):
	a, b = list(map(int, input().split()))
	if a != b:
		f = 1
	x.append(a)
if f == 1:
	print("rated")
elif sorted(x)[::-1] == x:
	print("maybe")
else:
	print("unrated")