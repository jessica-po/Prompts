n=int(input())
if n&1:
	print(-1)
else:
	D,R=[False]*(10**6),[0]*(10**6)
	i,j=0,0
	while True:
		D[j]=True
		R[i]=j
		i+=1
		if not D[(j+n)>>1]:
			j=(j+n)>>1
		elif not D[j>>1]:
			j=j>>1
		else:
			break
	print(" ".join(str(R[i]) for i in range(n,-1,-1)))