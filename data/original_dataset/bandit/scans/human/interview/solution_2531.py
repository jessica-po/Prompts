l=[]
for _ in range(int(input())):
	l.append(int(input()))
avg=0;l.sort()
for i in range(0,len(l)):
	j=0;n=len(l)-1
	while j<n:
		s=l[j]+l[n]
		if s>2*l[i]:
			n-=1
		elif s<2*l[i]:
			j+=1
		else:
			avg+=1;break
print(avg)