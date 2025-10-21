from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import defaultdict
from functools import reduce,cmp_to_key,lru_cache
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# import sys
# input = sys.stdin.readline
 
M = mod = 10**9 + 7 
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip().split()]
def st():return str(input().rstrip())[2:-1]
def val():return int(input().rstrip())
def li2():return [str(i)[2:-1] for i in input().rstrip().split()]
def li3():return [int(i) for i in st()]
 
 


graph = defaultdict(set)

n, k = li()
l = []
allwords = set()
for i in range(n):
    p = val()
    l1 = []
    for j in range(k):l1.append(st())

    allwords |= set(l1[-1])
    l.append([p, l1[:]])


l.sort(key = lambda x:x[0])
l = [i[1] for i in l]
if n == k == 1:
    print(''.join(set(l[0][0])))
    return


ingraph = defaultdict(int)

def match(a, b):
    for j in range(min(len(a), len(b))):
        if a[j] == b[j]:continue
        elif b[j] in graph[a[j]]:return
        else:
            graph[a[j]].add(b[j])
            ingraph[b[j]] += 1
            return
    if len(a) > len(b):
        print('IMPOSSIBLE')
        return

finl = []
for i in l:finl.extend(i)
l = finl

# for i in l:print(i)

for i in range(1, len(l)):
    match(l[i - 1], l[i])



# print(graph)
# print(ingraph)

if min([ingraph[j] for j in graph]) != 0:
    print('IMPOSSIBLE')
    return

ans = ''


d = deque()

for j in graph:
    if ingraph[j] == 0:
        d.append(j)

while d:
    node = d.popleft()
    ans += node

    for j in graph[node]:
        ingraph[j] -= 1
        if not ingraph[j]:d.append(j)


if len(ans) != len(allwords):
    print('IMPOSSIBLE')
    return
print(ans)