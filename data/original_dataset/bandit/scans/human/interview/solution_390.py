# import sys
# sys.stdin = open("F:\\Scripts\\input","r")
# sys.stdout = open("F:\\Scripts\\output","w")


MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n , a , b = I()
l = I()
cost = 0
m = min(a,b)
for i in range(n//2):
	if l[i] + l[n-i-1] == 1:
		print(-1)
		return
	if l[i] == 2 and l[n - i - 1] == 2:
		cost += 2*m
	elif l[i] == 2 or l[n - i - 1] == 2:
		if l[i] == 1 or l[n - i - 1] == 1:
			cost += b
		else:
			cost += a
if n%2 and l[n//2] == 2:
	cost += m
print(cost)