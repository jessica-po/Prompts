N,M=map(int, input().split())
AB=sorted([list(map(int, input().split())) for _ in range(N)])

cnt=0
gokei=0
for ab in AB:
	if M-cnt>ab[1]:
		gokei+=ab[1]*ab[0]
		cnt+=ab[1]
	else:
		gokei+=(M-cnt)*ab[0]
		cnt+=M-cnt
	
	if cnt==M:
		print(gokei)
		return