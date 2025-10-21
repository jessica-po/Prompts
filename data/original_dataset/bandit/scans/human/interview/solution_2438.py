n = int(input())
s = input()
tab = []
count = 1
for i in range(1, n):
	if s[i] == s[i-1]:
		count += 1
	else:
		if count > 0:
			tab.append(count)
		count = 1
if count > 0:
	tab.append(count)
dis = 0
k = len(tab)
if k == 0 or k == 1:
	dis = 0
else:
	dis += tab[1]
	dis += tab[-2]
	dis -= (k-1)
	for i in range(1, k - 1):
		dis += tab[i-1]
		dis += tab[i+1]
print(n*(n-1)//2 - dis)