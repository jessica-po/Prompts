def __starting_point():
	a=[int(x) for x in input().split()]
	N=a[0]
	A=a[1]
	B=a[2]
	K=a[3]
	s=input()
	mod = 1000000009
	Q = pow(B*pow(A,mod-2,mod)%mod,K,mod)
	if Q!=1:
		D = (pow(Q,(N+1)//K,mod)-1)*pow(Q-1,mod-2,mod)%mod
	else:
		D = (N+1)//K
	ans=0
	C = pow(A,N,mod)
	A=pow(A,mod-2,mod)
	for i in range(K):
		if s[i]=='+':
			ans=(ans+C*D)%mod
		else:
			ans=(ans-C*D)%mod
		C=C*B*A%mod
	print((ans%mod+mod)%mod)
__starting_point()