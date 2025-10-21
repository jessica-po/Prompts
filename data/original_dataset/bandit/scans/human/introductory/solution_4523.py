import sys
import math
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return list(map(int, sys.stdin.readline().split()))

def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
	n = II()
	a = sorted(LI())
	boo = True
	for i in range(1,n):
		if a[i]-a[i-1]>1:
			boo = False
			break
	print("YES" if boo else "NO")