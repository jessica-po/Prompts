n = int(input())

ls = [input() for _ in range(n)]

balance = [[0, 0] for _ in range(n)]

for i in range(n):
	for j in range(len(ls[i])):
		balance[i][0] = balance[i][0] + (1 if ls[i][j] == '(' else -1)
		balance[i][1] = min(balance[i][1], balance[i][0])

balance2 = []

for i in range(n):
	if balance[i][0] < 0:
		if balance[i][1] >= balance[i][0]:
			balance2.append(balance[i][0])
	if balance[i][0] >= 0:
		if balance[i][1] >= 0:
			balance2.append(balance[i][0])

balance2.sort()


answer = 0

i, j = 0, len(balance2) - 1

while i < j:
	if balance2[i] + balance2[j] == 0:
		answer += 1
		i += 1
		j -= 1
	elif balance2[i] + balance2[j] < 0:
		i += 1
	elif balance2[i] + balance2[j] > 0:
		j -= 1 

print(answer)