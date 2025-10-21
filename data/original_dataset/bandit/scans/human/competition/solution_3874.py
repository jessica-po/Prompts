m,n=list(map(int,input().split()))
s=[input().strip() for i in range(m)]
a=list([int(x)-1 for x in input().split()])
stmpl=s[a[0]]
f=1
def peres(s1,s2):
	return ''.join([i if i==j else '?' for i,j in zip(s1,s2)])
for i in a:
	if len(stmpl)!=len(s[i]):
		f=0
		break
	stmpl=peres(stmpl,s[i])
for i,e in enumerate(s):
	if i in a:
		continue
	if len(stmpl)==len(e) and stmpl==peres(stmpl,e):
		f=0
		break
if f:
	print('Yes')
	print(stmpl)
else:
	print('No')