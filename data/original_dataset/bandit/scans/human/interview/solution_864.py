n, k = map(int, input().split())
a = list(map(int, input().split()))
day = 1
def poss(day):
	q = 0
	mp = dict()
	for el in a:
		if el not in mp:
			mp[el] = 1
		else:
			mp[el] += 1
	for el in mp:
		q += mp[el] // day
	return q >= n

while poss(day):
	day += 1

print(day - 1)