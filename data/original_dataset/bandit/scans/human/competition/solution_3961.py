n,a= int(input()),list(map(int,input().split()))
f,m= [0]*(n+1),10**9+7
for i in range(n):
	if a[i]==i+1:
		f[i+1]=f[i]+2
	else:
		f[i+1]=(2+f[i]*2-f[a[i]-1])%m
print(f[n]%m)