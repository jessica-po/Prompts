n = int(input())

a = list(map(int, input().split()))

m = int(input())

q = list(map(int, input().split()))

a.sort()

s = sum(a)

for qi in q:
	print(s - a[-qi])