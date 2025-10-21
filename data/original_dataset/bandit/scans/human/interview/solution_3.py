from collections import defaultdict as dd
import math
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))


n, q=mi()

ints=[]


for _ in range(q):
	st, end=mi()
	ints.append((st,end))


coverage=[10]+[0]*n

for st, end in ints:
	for i in range(st,end+1):
		coverage[i]+=1

total=-1

for val in coverage:
	if not val==0:
		total+=1

singlecount=0
doublecount=0

singles=[0]*(n+1)
#print(total)
doubles=[0]*(n+1)
for i in range(len(coverage)):
	#print(i,singles)
	if coverage[i]==1:
		singlecount+=1
	if coverage[i]==2:
		doublecount+=1
	singles[i]=singlecount
	doubles[i]=doublecount
maxtotal=0
for i in range(len(ints)):
	for j in range(i+1, len(ints)):
		st1=min(ints[i][0],ints[j][0])
		end1=min(ints[i][1],ints[j][1])
		st2, end2=max(ints[i][0],ints[j][0]), max(ints[i][1],ints[j][1])
		#assume st1<=st2
		if end1<st2:
			curtotal=total-(singles[end1]-singles[st1-1])-(singles[end2]-singles[st2-1])
		elif end1<end2:
			curtotal=total-(singles[st2-1]-singles[st1-1])-(doubles[end1]-doubles[st2-1])-(singles[end2]-singles[end1])
		else:
			curtotal=total-(singles[st2-1]-singles[st1-1])-(doubles[end2]-doubles[st2-1])-(singles[end1]-singles[end2])
		maxtotal=max(maxtotal,curtotal)

print(maxtotal)