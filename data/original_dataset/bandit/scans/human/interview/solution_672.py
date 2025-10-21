# fin = open("input.txt")
# a, b = map(int, fin.readline().split())
a, b = list(map(int, input().split()))
a2 = a - b
if a2 == 0:
	print("infinity")
else:
	Count = 0
	i = 1
	while i ** 2 <= a2:
		Count += (a2 % i == 0 and i > b) + (a2 % i == 0 and a2 // i > b and i != a2 // i)
		i += 1
	print(Count)