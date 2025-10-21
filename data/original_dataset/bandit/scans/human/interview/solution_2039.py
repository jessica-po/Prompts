'''input
4
1 5 2 5
'''
n = int(input())
a = list(map(int, input().split()))
t = 0
for x in range(1, n-1):
	if a[x] > a[x-1] and a[x] > a[x+1]:
		t += 1
	elif a[x] < a[x-1] and a[x] < a[x+1]:
		t += 1
print(t)