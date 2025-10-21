L=input()
r=0
for l in L:
	r+=int(l)
print('Yes' if r%9==0 else 'No')