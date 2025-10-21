import sys
input = sys.stdin.readline

def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n,k=map(int,input().split())
	for i in range(2,n+1):
		if n%i==0:
			num=i
			break
	print (n+i+2*(k-1))