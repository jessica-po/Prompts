n = int(input())
u = [int(u) for u in input().split()]

NMAX = 100005

suma = [0 for _ in range(NMAX)]
total = [0 for _ in range(NMAX)]

diferentes = 0
sol = 0
maximo = 1

for i, v in enumerate(u):
	if total[v] == 0:
		diferentes += 1
	else:
		suma[total[v]] -= 1
	total[v] += 1
	suma[total[v]] += 1

	maximo = max(maximo, total[v])

	#print(i, v, ":", diferentes)
	#print(suma)
	#print(total)
	#print(maximo, ":", suma[maximo], suma[maximo+1], diferentes-1)
	#print(maximo, ":", suma[maximo-1], suma[maximo], diferentes-1)

	if diferentes <= 1:
		sol = i

	if suma[maximo-1] == diferentes-1 and suma[maximo] == 1:
		sol = i

	if suma[maximo] == diferentes-1 and suma[1] == 1:
		sol = i

	if suma[1] == diferentes:
		sol = i
	
	#print("SOL", sol)

print(sol+1)