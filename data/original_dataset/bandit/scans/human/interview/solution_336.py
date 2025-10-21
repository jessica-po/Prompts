n, a, b, c, d= [int(i) for i in input().split()]
o = 0
for i in range(1, n+1):
	if i+b-c>0 and i+b-c<=n:
		if i+a-d>0 and i+a-d<=n:
			if i+a+b-c-d>0 and i+a+b-c-d<=n:
				o+=1
print(o*n)