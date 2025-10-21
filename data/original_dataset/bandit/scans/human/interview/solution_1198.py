str=input().split()
n=int(str[0])
len=int(str[1])
a=[]
Q=[]
F=[]
for i in range(0,n+1):
	a.append(0)
	Q.append(0)
	F.append(0)
sum=0
h=1
t=0
str=input().split()
for i in range(1,n+1):
	a[i]=int(str[i-1])
	sum+=a[i]
	#print (sum)
	while h<=t and Q[h]<=i-len:
		h=h+1
	while h<=t and a[i]<=a[Q[t]]:
		t=t-1
	t=t+1;Q[t]=i;
	if (i<len) :
		F[i]=0
	else :
		F[i]=F[i-len]+a[Q[h]]
	F[i]=max(F[i],F[i-1])
		
print(sum-F[n])