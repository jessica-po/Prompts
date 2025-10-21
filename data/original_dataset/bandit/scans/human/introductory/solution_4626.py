t=int(input())
for nt in range(t):
	a,b,c=map(int,input().split())
	print (max(0,abs(a-b)+abs(b-c)+abs(a-c)-4))