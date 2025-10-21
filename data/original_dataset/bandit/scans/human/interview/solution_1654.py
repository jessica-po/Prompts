s = input()
t = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
dabc ={}
for i in range(26):
	dabc[abc[i]] = i

lt = {}
ls = {}
dd = {}
ls['?'] = 0
for i in abc:
	lt[i] = 0
	ls[i] = 0
	dd[i] = 0
for letter in t:
	lt[letter] += 1
for letter in s:
	ls[letter] +=1

X = ls['?']
def check(ans):
	nonlocal ls, lt, abc, X
	return -sum(min(0, ls[l] - lt[l] * ans) for l in abc) <= X

start, end = [0, 2000000]
i = 0
while start < end:
	st = start + end
	ans = (st + st%2)//2
	if check(ans):
		start = ans
	else:
		end = ans - 1
ans = start


for letter in abc:
	dd[letter] = max(0, lt[letter] * ans - ls[letter])
	X -= max(0, lt[letter] * ans - ls[letter])

s1 = ['']
j = 0
for i in s:
	if i != '?':
		s1.append(i)
	else:
		try:
			while dd[abc[j]] == 0:
				j +=1
			s1.append(abc[j])
			dd[abc[j]] -= 1
		except:
			s1.append('z')

print(''.join(s1))