'''input
5 20
45 -6
34 -15
10 34
1 27
40 -45


'''
import sys
from collections import defaultdict as dd

mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())


n, r = ri()

eventspos = []
eventsneg = []
for i in range(n):
	temp =ri()
	if temp[1]>=0:
		eventspos.append(temp)
	else:
		eventsneg.append(temp)

eventspos.sort()
eventsneg.sort(key = lambda x: x[0]+x[1])
eventsneg.reverse()

status =1

ans=0 

for i in range(len(eventspos)):
	if eventspos[i][0] <= r:
		r+= eventspos[i][1]
		ans+=1
	else:
		status = 0


check = [0 for i in range(r+1)]

#print(eventsneg)

for i in range(len(eventsneg)):
	for j in range(eventsneg[i][0] , r+1):
		if j+eventsneg[i][1]>=0:
			check[j+eventsneg[i][1]] = max(check[j+eventsneg[i][1]] , check[j]+1) 



# if status and r>=0 and sum(check)==len(check):
# 	print("YES")
# else:
# 	print("NO")

#print(eventsneg,eventspos)

print(max(check) + ans	)