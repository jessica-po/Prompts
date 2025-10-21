import heapq as hq
from queue import PriorityQueue

import math
n,m,r, k= input().split()
N = int(n)
M = int(m)
R = int(r)
K = int(k)

q = PriorityQueue()



for i in range(1,math.floor((N+1)/2) + 1):
    maxi = min(min(i,N-i+1),min(R,N-R+1)) * min(min(R,M-R+1),math.ceil(M/2))
    num = M - (2 * min(min(R,M-R+1),math.ceil(M/2))-2)
    mult = 2
    if(i > math.floor(N/2)):
        mult = 1
    q.put((-maxi,num * mult,i))
    #print(str(maxi) + " " + str(num) + " " + str(mult))


ans = 0
while(K > 0):
    pop = q.get()
    #print(pop)
    a = -1 * pop[0]
    b = pop[1]
    c = pop[2]
    d = min(min(c,N-c+1),min(R,N-R+1))
    if(d != a):
       # if(q.)
       # if(q.get(-(a - d)) != )
        mult = 2
        if (c > N / 2):
            mult = 1
        q.put((-(a - d),2*mult,c))
    ans += a * min(b,K)
    K -= b;

tot = (N-R+1) * (M-R+1)
#print("ANS = " + str(ans))
#print("FINANS = " + str(ans/tot))
print(str(ans/tot))


'''

d = []
for i in range(0,N):
    d.append([])
    for j in range(0,M):
        d[i].append(0)

tot = 0
for i in range(0,N-R+1):
    for j in range(0,M-R+1):
        for k in range(i,i+R):
            for l in range(j,j+R):
                d[k][l] += 1
                tot += 1


print(N-R+1)*(M-R+1) * (R*R)
print(tot)
print()
for i in d:
    print(i)

'''