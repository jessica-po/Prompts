def l2i(s):
	return [int(i) for i in s.split()]
a, b=l2i(input())
t=0
while (a<=b):
	a*=3
	b*=2
	t+=1
print(t)