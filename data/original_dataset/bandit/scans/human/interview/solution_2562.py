n,N,MOD,ans=int(input()),int(1e6+5),int(1e9+7),0
cnt,pw,f=[0]*int(N),[1]*(n+1),[0]*int(N)
for i in range(n):
	pw[i+1]=pw[i]*2%MOD
for i in input().split():
	cnt[int(i)]+=1
for i in reversed(range(2,N)):
	t=sum([cnt[j] for j in range(i,N,i)])
	if t:
		f[i]=t*pw[t-1]%MOD
		for j in range(i*2,N,i):
			f[i]=(f[i]-f[j])%MOD
		ans+=i*f[i]%MOD
print(ans%MOD)