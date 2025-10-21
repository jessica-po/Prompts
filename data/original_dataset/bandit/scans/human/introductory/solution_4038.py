n=int(input())
a=list(map(int,input().split()))

c=[0]*1001

for i in range (len(a)):
	c[a[i]]+=1

sym=0
sin=0

for i in range (1001):
	sym+=(c[i]//4)
	if(c[i]%2==1):
		sin+=1

if(n%2==0 and sym==((n*n)//4)):
	mat= [([0]*(n//2)) for i in range (n//2)]
	ar=[]
	for i in range (1001):
		while(c[i]>=4):
			ar.append(i)
			c[i]-=4
	
	k=0
	for i in range (n//2):
		for j in range (n//2):
			mat[i][j]=ar[k]
			k+=1

	newm=[([0]*n) for i in range (n)]
	for i in range (n//2):
		for j in range (n//2):
			newm[i][j]=mat[i][j]
			newm[n-i-1][j]=mat[i][j]
			newm[n-i-1][n-j-1]=mat[i][j]
			newm[i][n-j-1]=mat[i][j]

	print("YES")
	for i in range (n):
		for j in range (n):
			print(newm[i][j],end=" ")
		print()

	
elif(n%2==1 and (((sym>=(((n//2) *(n//2)) ) ) and (sin==1)))):
	mat= [([0]*(n//2)) for i in range (n//2)]
	ar=[]
	for i in range (1001):
		while(c[i]>=4):
			ar.append(i)
			c[i]-=4
	
	k=0
	for i in range (n//2):
		for j in range (n//2):
			mat[i][j]=ar[k]
			ar.pop(k)

	newm=[([0]*n) for i in range (n)]
	for i in range (n//2):
		for j in range (n//2):
			newm[i][j]=mat[i][j]
			newm[n-i-1][j]=mat[i][j]
			newm[n-i-1][n-j-1]=mat[i][j]
			newm[i][n-j-1]=mat[i][j]

	na=len(ar)
	ar2=[]
	for i in range (na):
		ar2.append(ar[i])
		ar2.append(ar[i])

	for i in range (1001):
		while(c[i]>=2):
			ar2.append(i)
			c[i]-=2

	#print(ar)
	for i in range (n//2):
		newm[n//2 ][i]=ar2[0]
		newm[n//2 ][n-i-1]=ar2[0]
		ar2.pop(0)
		newm[i][n//2 ]=ar2[0]
		newm[n-i-1][n//2 ]=ar2[0]
		ar2.pop(0)

	for i in range (1001):
		if(c[i]==1):
			newm[n//2][n//2]=i
	
	print("YES")
	for i in range (n):
		for j in range (n):
			print(newm[i][j],end=" ")
		print()

else:
	print("NO")