from collections import defaultdict as dd
import math
import sys
#input=sys.stdin.readline
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))

n,m=mi()

quilt=[]
for i in range(n):
	quilt.append(li())
def getflags(column):
	flags=set()
	breaks=[0]
	for i in range(0,len(column)-1):
		if not column[i]==column[i+1]:
			breaks.append(i+1)
	breaks.append(len(column))	
	#print(breaks)
	for j in range(1,len(breaks)-2):
		midlength=breaks[j+1]-breaks[j]
		firstlength=breaks[j]-breaks[j-1]
		endlength=breaks[j+2]-breaks[j+1]
		if midlength<=firstlength and midlength<=endlength:
			flags.add(((breaks[j+1],breaks[j]), (column[breaks[j+1]], column[breaks[j]],column[breaks[j-1]])))
	return flags

flagdicts=[0]*m

for i in range(m):
	col=[row[i] for row in quilt]
	flagdicts[i]=getflags(col)
total=0
#print(flagdicts)
for i in range(m):
	for flag in flagdicts[i]:
		k=1
		
		while i+k<m and flag in flagdicts[i+k]:
			k+=1
			#print(flagdicts[i+k])
			#flagdicts[i+k].remove(flag)
		for j in range(1,k):
			flagdicts[i+j].remove(flag)
		total+=k*(k+1)//2		
print(total)