q = int(input())
for _ in range(q):
	n,m,k = map(int,input().split())
	player = n//k
	jok_pla = min(n//k, m)
	jok_re = m-jok_pla
	maksi = (jok_re +k-2)//(k-1)
	print(jok_pla-maksi)