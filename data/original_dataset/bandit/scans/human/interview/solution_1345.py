n=int(input())
a=list(map(int,input().split(' ')))

temp_sgn=1
sgns=[]
curr_sum=0
for i in range(n):
	if(curr_sum>=a[n-i-1]):
		sgns.append(1)
		sgns.append(-1)
		curr_sum-=a[n-i-1]
	else:
		sgns.append(-1)
		sgns.append(1)
		curr_sum-=a[n-i-1]
		curr_sum*=-1
sgns.reverse()
ans=[]
for i in range(2*n):
	if(i%2==0):
		ans.append(temp_sgn*sgns[i])
	else:
		temp_sgn*=sgns[i]
for x in ans:
	if(x==1):
		print('+',end='')
	else:
		print('-',end='')