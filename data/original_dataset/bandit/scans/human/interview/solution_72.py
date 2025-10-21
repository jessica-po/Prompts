turns = int(input())
s0 = input()
s1 = input()
s2 = input()

d0 = dict()
d1 = dict()
d2 = dict()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for char in alphabet:
	d0[char] = 0
	d1[char] = 0
	d2[char] = 0

for char in s0:
	d0[char] += 1
for char in s1:
	d1[char] += 1
for char in s2:
	d2[char] += 1	

m0 = max([d0[char] for char in alphabet])
m1 = max([d1[char] for char in alphabet])
m2 = max([d2[char] for char in alphabet])

l0 = len(s0)
l1 = len(s1)
l2 = len(s2)

if turns == 1 and m0 == l0:
	score0 = m0 - 1
else:
	score0 = min(l0,m0+turns)

if turns == 1 and m1 == l1:
	score1 = m1 - 1
else:
	score1 = min(l1,m1+turns)

if turns == 1 and m2 == l2:
	score2 = m2 - 1
else:
	score2 = min(l2,m2+turns)
	
scores = [score0,score1,score2]
bestscore = max(scores)

winnerlist = [i for i in range(3) if scores[i] == bestscore]
if len(winnerlist) > 1:
	print('Draw')
else:
	print(['Kuro','Shiro','Katie'][winnerlist[0]])