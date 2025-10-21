from collections import defaultdict as dd
import math
import heapq
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))

n, m=mi()
A=[]
for i in range(n):
	A.append(lm())

B=[]
for i in range(n):
	B.append(lm())

def check(A,B):
	for i in range(n):
		count=0
		for j in range(m):
			count+=abs(A[i][j]-B[i][j])

		if not count%2==0:
			return 'No'

	for j in range(m):
		count=0
		for i in range(n):
			count+=abs(A[i][j]-B[i][j])
		if not count%2==0:
			return 'No'

	return 'Yes'

print(check(A,B))