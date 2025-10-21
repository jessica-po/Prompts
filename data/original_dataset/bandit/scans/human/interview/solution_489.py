n=int(input())
inp=input().split()
l=[]
for val in inp:
	l.append(int(val))
l.sort()
count=3
while(count<n and l[count]==l[count-1]):
	count+=1
if(l[2]!=l[1]):
	print(count-2)
elif(l[2]!=l[0]):
	print(((count-1)*(count-2))//2)
else:
	print((count*(count-1)*(count-2))//6)