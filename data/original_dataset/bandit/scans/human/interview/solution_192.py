x, y = list(map(int, input().split()))
x, y = y, x
A = x
B = x
curr = x
count = 0
while curr < y:
	curr = B + A - 1
	A, B = B, curr
	count += 1
count += 2
print(count)