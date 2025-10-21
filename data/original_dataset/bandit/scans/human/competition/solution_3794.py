import sys

def gcd(l):
	if len(l)==0:
		return 0
	if len(l)==1:
		return l[0]
	if len(l)==2:                                   
		if l[1]==0:
			return l[0]  
		return gcd([l[1],l[0]%l[1]])
	return gcd([gcd(l[:-1]),l[-1]])
		
def brute_force(l1,l2,l,sol):                   
	if len(l)==0:
		g1=gcd(l1)
		g2=gcd(l2)
		return g1==1 and g2==1,sol
	
	res,s=brute_force(l1+[l[0]],l2,l[1:],sol+[1])
	if res:
		return True,s
	return brute_force(l1,l2+[l[0]],l[1:],sol+[2])

def factor(n):
	res=[]
	i=2
	while i*i<=n:
		if n%i==0:
			res.append(i)
		while n%i==0:
			n=int(n/i)
		i+=1

	if n!=1:
		res.append(n)

	return res

def dumpsol(sol):
	for v in sol:
		print(v,end=' ')

n=int(sys.stdin.readline())
l=sys.stdin.readline().strip().split(" ")[0:n]
l=[int(x) for x in l]
if n<12:
	ret,sol=brute_force([],[],l,[])
	if ret:
		print("YES")
		dumpsol(sol)
	else:
		print("NO")
	return

factors={}
for i in range(10):
	for key in factor(l[i]):
		factors[key]=0

flists={}
for f in factors:
	flists[f]=[]
	pos=0
	found=False
	for v in l:
		if v%f!=0:
			found=True
			factors[f]+=1
			flists[f].append(pos)
			if (factors[f]>9):
				break
		pos+=1
	if not found:
		print("NO")
		return

oftf=[]
isoftf={}
for f in factors:
	if factors[f]==0:
		print("NO")
		return

	if factors[f]<10:
		oftf.append(f)
		isoftf[f]=1

#print(oftf)

sol=[1 for i in range(len(l))]
x=l[0]
sol[0]=2
oxf=factor(x)
#print(oxf)
xf=[]
nxf=0
isxoftf={}
for f in oxf:
	if f in isoftf:
		nxf+=1
		isxoftf[f]=1
		xf.append(f)
	else:
		sol[flists[f][0]]=2

nonxf=[]
for f in oftf:
	if not f in isxoftf:
		nonxf.append(f)

masks={}
pos=0

#print(xf)
#print(nonxf)

for f in xf+nonxf:
	for v in flists[f]:
		if not v in masks:	
			masks[v]=0
		masks[v]|=1<<pos
	pos+=1

vals=[{} for i in range(len(masks)+1)]
vals[0][0]=0
pos=0
mlist=[]
for mask in masks:
	mlist.append(mask)
	cmask=masks[mask]
	cmask1=cmask<<10
	#print(vals)
	for v in vals[pos]:
		vals[pos+1][v|cmask]=v
		# first number is always in group2
		if (mask!=0):
			vals[pos+1][v|cmask1]=v
	pos+=1	

#print(vals)
#print(masks)
#print(sol)

test_val=((1<<len(xf))-1)|(((1<<len(oftf))-1)<<10)
#print(test_val)
for v in vals[pos]:
	if (v&test_val)==test_val:
		print("YES")

		#print(pos)
		while (pos!=0):
			#print(v)
			#print(vals[pos])
			nv=vals[pos][v]
			#print(nv)
			if (nv^v<1024 and nv^v!=0):
				sol[mlist[pos-1]]=2
			v=nv
			pos-=1

		dumpsol(sol)
		return

print("NO")

#print(oftf)
#print(masks)