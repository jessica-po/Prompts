def mi():
	return map(int, input().split())

from collections import Counter
n = list(mi())[0]
a = Counter(list(mi()))
ma= -1
for i in a:
	if a[i]>ma:
		ma = a[i]
print (ma)