n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
solved=[0 for i in range(5)]
score=[0 for i in range(5)]
for i in range(n):
	for j in range(5):
		solved[j]+=int(a[i][j]>-1)
for k in range(31*n+1):
	for i in range(5):
		tot=n+k
		cur=solved[i]
		if a[0][i]>-1 and a[1][i]>-1 and a[0][i]>a[1][i]:
			cur+=k
		score[i]=500
		while score[i]<3000 and 2*cur<=tot:
			cur*=2;
			score[i]+=500
	res=[0,0]
	for j in range(2):
		for i in range(5):
			if a[j][i]>-1:
				res[j]+=score[i]/250*(250-a[j][i])
	if res[0]>res[1]:
		print(k)
		return
print("-1")