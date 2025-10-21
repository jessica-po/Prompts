import sys
import math
def II():
	return int(sys.stdin.readline())
 
def LI():
	return list(map(int, sys.stdin.readline().split()))
 
def MI():
	return map(int, sys.stdin.readline().split())
 
def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
	a,b,c,d = MI()
	print(max(a+b,c+d))