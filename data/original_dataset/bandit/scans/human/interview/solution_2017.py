import sys
from collections import defaultdict
 
class BIT():
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n
    
    def _get_sum(self, r):
        '''
        sum on interval [0, r)
        '''
        result = 0
        while r > 0:
            result += self.tree[r-1]
            r &= (r - 1)
        return result
    
    def get_sum(self, l, r):
        '''
        sum on interval [l, r)
        '''
        return self._get_sum(r) - self._get_sum(l)
    
    def add(self, i, value=1):
        while i < self.n:
            self.tree[i] += value
            i |= (i + 1)

reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
swaps = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    swaps.append(i)
    swaps.append(j)

pos = defaultdict(list)
for i, val in enumerate(swaps):
    pos[val].append(i)

c = 0
prev = -1
compr = [0] * (2*n)
decompr = {}
for val in sorted(swaps):
    if prev == val: continue
    for j in pos[val]:
        compr[j] = c
    decompr[c] = val
    c += 1
    prev = val

arr = list(range(c))
for t in range(n):
    i, j = compr[t<<1], compr[t<<1|1]
    arr[i], arr[j] = arr[j], arr[i]

bit = BIT(c)
total_inv = 0
for i, val in enumerate(arr):
    total_inv += bit.get_sum(val+1, c)
    if i != val:
        total_inv += abs(decompr[val] - decompr[i]) - abs(val - i)
    bit.add(val)
print(total_inv)