#      Codeforces Round #487 (Div. 2)import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    
import bisect
 
            
    
N,L,WM  = getIntList()

z = {}
z[-1] = {1:[], -1:[]}
z[0] = {1:[], -1:[]}
z[1] = {1:[], -1:[]}
for i in range(N):
    x0,v = getIntList()
    t = (x0,v)
    if x0+L <=0:
        z[-1][v].append(t)
    elif x0>=0:
        z[1][v].append(t)
    else:
        z[0][v].append(t)
res = 0

res += len(z[-1][1] ) * len(z[ 1][-1] )
res += len(z[0][1] ) * len(z[ 1][-1] )
res += len(z[-1][1] ) * len(z[ 0][-1] )

if WM==1:
    print(res)
    return

z[1][-1].sort()
z[-1][1].sort()
#print(z[-1][1])
tn = len(z[1][-1])
for t in z[1][1]:
    g = (-WM-1) * t[0] / (-WM+1) - L
    g = max(g, t[0]+ 0.5)
    p = bisect.bisect_right(z[1][-1], (g,2) )
    res +=  tn-p 
    
tn = len(z[-1][1])
for t in z[-1][-1]:
    g = (WM+1) * (t[0] + L)/ (WM-1)
    g = min(g, t[0] - 0.1)
    
    p = bisect.bisect_left(z[-1][1], (g,-2) )
    res +=  p 

print(res)