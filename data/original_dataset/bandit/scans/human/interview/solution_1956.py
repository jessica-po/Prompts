def f(s,e):
	if e%2:
		return 1-s%2
	elif s*2>e:
		return s%2
	else:
		return g(s,e//2)
def g(s,e):
	if 2*s>e:
		return 1
	else:
		return f(s,e//2)

a=[tuple(map(int,input().split())) for i in range(int(input()))]
b=1
for i in a:
	b1=g(*i)|(f(*i)<<1)
	b=b1^3 if b==2 else b1
	if b==0:
		print('0 0')
		return
	elif b==3:
		print('1 1')
		return
		
if b==2:
	print('1 0')
else:
	print('0 1')