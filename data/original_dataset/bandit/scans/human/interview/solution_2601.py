input=__import__('sys').stdin.readline
for _ in range(int(input())):
	n=int(input())
	s=list(map(int,input().split()))
	print('YNEOS'[sum(a>b for a,b in zip(s,s[1:]))==n-1::2])