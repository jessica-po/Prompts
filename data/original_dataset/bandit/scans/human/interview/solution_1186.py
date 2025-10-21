def test(x, i):
	i = list(i)
	ok = True
	for j in range(x):
		if (i[j] == j+1 or (i[j]&(j+1) != 0)):
			ok = False
	if ok:
		print(i)

def comp(n):
	return 2**len(bin(n)[2:])-1-n

n = int(input())
nn = n
if (n%2 == 0):
	x = []
	while (n != 0):
		#add n to comp(n) to the front of x
		for i in range(comp(n), n+1):
			x.append(i)
		n = comp(n)-1

	x.reverse()
	print("YES")
	print(' '.join([str(i) for i in x]))
else:
	print("NO")

pow2 = [2**i for i in range(20)]
def make(n):
	if n <= 5: return []
	if n == 6: return [3, 6, 1, 5, 4, 2]
	if n == 7: return [3, 6, 1, 5, 4, 7, 2]
	if n in pow2:
		return []
	shift = 2**(len(bin(n)[2:])-1)
	array = [i for i in range(shift, n+1)]
	array = array[1:] + [array[0]]
	return make(shift-1) + array

n = nn
k = make(n)
if k == []:
	print("NO")
else:
	print("YES")
	print(' '.join([str(i) for i in k]))