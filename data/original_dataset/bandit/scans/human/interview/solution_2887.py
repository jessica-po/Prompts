def solve():
	n=int(input())
	l1=list(map(int,input().split()))
	l2=list(map(int,input().split()))
	ans=[]
	for i in range (n):
		c=0
		for j in range (i+1):
			if l1[j]<=l2[i]:
				c+=l1[j]
				l1[j]=0
			else:
				l1[j]-=l2[i]
				c+=l2[i]
		ans.append(c)
	print(*ans)
solve()