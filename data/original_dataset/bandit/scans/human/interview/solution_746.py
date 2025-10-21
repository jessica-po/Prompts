import math
a, b = [int(i) for i in input().split()]
n = int(input())
o = []
for i in range(n):
	x, y, z = [int(i) for i in input().split()]
	o.append(math.sqrt((x-a)**2+(y-b)**2)/z)
print(min(o))