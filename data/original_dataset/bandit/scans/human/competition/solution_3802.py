# coding=utf-8
from functools import reduce

a = input()
b = input()
c = input()

alen = len(a)
blen = len(b)
clen = len(c)

kmpnext = [0]*(clen+1)
i = 1
j = 0
while i < clen:
	while j > 0 and c[i]!=c[j]:
		j = kmpnext[j]
	if c[i] == c[j]:
		j+=1
	kmpnext[i+1] = j
	i+=1
#print(kmpnext)

f = [[[0 for i in range(clen+2)] for i in range(blen+2)] for i in range(alen+2)]
g = [[[0 for i in range(clen+2)] for i in range(blen+2)] for i in range(alen+2)]
h = [[[0 for i in range(clen+2)] for i in range(blen+2)] for i in range(alen+2)]

f[0][0][0] = 0
g[0][0][0] = (-1,-1,-1)
h[0][0][0] = 1
m = (0,0,0)

for i in range(alen):
	for j in range(blen):
		for k in range(clen):
			if h[i][j][k] == 0:
				#print(i,j,k)
				continue
			if f[i+1][j][k] < f[i][j][k] or h[i+1][j][0] == 0:
				f[i+1][j][k] = f[i][j][k]
				g[i+1][j][k] = g[i][j][k]
				h[i+1][j][k] = 1
			if f[i][j+1][k] < f[i][j][k] or h[i][j+1][0] == 0:
				f[i][j+1][k] = f[i][j][k]
				g[i][j+1][k] = g[i][j][k]
				h[i][j+1][k] = 1

			if a[i] == b[j]:
				#print(i,j,a[i],b[j])
				kt = k
				while kt != 0 and a[i] != c[kt]:
					kt = kmpnext[kt]
				if a[i] == c[kt]:
					if f[i+1][j+1][kt+1] < f[i][j][k] + 1:
						f[i+1][j+1][kt+1] = f[i][j][k] + 1
						g[i+1][j+1][kt+1] = (i,j,k)
						h[i+1][j+1][kt+1] = 1
				else:
					if f[i+1][j+1][0] < f[i][j][k] + 1:
						f[i+1][j+1][0] = f[i][j][k] + 1
						g[i+1][j+1][0] = (i,j,k)
						h[i+1][j+1][0] = 1

			#print(i,j,k,f[i][j][k],g[i][j][k])

for i in range(alen+1):
	for j in range(blen+1):
		for k in range(clen):
			if f[i][j][k] > f[m[0]][m[1]][m[2]]:
				m = (i,j,k)
if f[m[0]][m[1]][m[2]] == 0:
	print(0)
else:
	ans = ""
	t = m
	t = g[t[0]][t[1]][t[2]]
	while t != (-1,-1,-1):
		ans = a[t[0]] + ans
		t = g[t[0]][t[1]][t[2]]
	print(ans)