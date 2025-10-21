import sys
import bisect
input = sys.stdin.readline

trips = int(input())
dyn = [int(input()) for i in range(trips)]

cmap = [0,20] + [0 for i in range(trips-1)]

for i in range(2,trips+1):
    cmap[i] = min(cmap[i-1] + 20,
                  cmap[bisect.bisect_left(dyn,dyn[i-1]-89)] + 50,
                  cmap[bisect.bisect_left(dyn,dyn[i-1]-1439)] + 120)

for i in range(1,trips+1):
    print(cmap[i]-cmap[i-1])