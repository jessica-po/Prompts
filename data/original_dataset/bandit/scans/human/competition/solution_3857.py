n = int(input())
ar = list(map(int,input().split(' ')))
ar.sort()
s=[]
for i in ar:
	s.sort(reverse=True)
	for j in range(len(s)):
		if i>=s[j]:
			s[j]+=1
			break
	else:
		s.append(1)
print(len(s))