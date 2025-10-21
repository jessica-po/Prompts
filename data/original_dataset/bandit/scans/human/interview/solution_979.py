from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
l = list(map(int,input().split()))
if n > m:
	print(0)
else:
	res = 1
	for i in range(n-1):
		for j in range(i+1,n):
			res = ((res*abs(l[i]-l[j])) % m)
	print(res%m)