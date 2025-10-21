k,n,w = map(int,input().split())

x = (w)*(w+1)//2 * k

y = x - n

if(y >= 0):
	print(y)
else:
	print(0)