m = 1000000007
n = int(input())
a = map(int, input().split())
t1, t2 = 0, 0
for i in a:
	if i == 1:
		t1 += 1
	else:
		t2 += 1
a = [1, 2]
for i in range(3, t1+1):
	a = a[::-1]
	a[1] = (a[0]+(i-1)*a[1])%m
if not t1 or t1 == 1:
	a[1] = 1
for i in range(t1+1, n+1):
	a[1] = a[1]*i%m
print(a[1])