import sys

class SegmTree():
    def __init__(self, array=None):
        size = len(array)
        N = 1
        while N < size:
            N <<= 1
        self.N = N
        self.tree = [0] * (2*self.N)
        for i in range(size):
            self.tree[i+self.N] = array[i]
        self.build()

    def build(self):
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
 
    def add(self, i, value=1):
        i += self.N
        while i > 0:
            self.tree[i] += value
            i >>= 1
    
    def get_sum(self, l, r):
        N = self.N
        l += N
        r += N
        result = 0
        while l < r:
            if l & 1:
                result += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                result += self.tree[r]
            l >>= 1
            r >>= 1
        return result
    
    def find_kth_nonzero(self, k):
        i = 1
        if k < 1 or k > self.tree[1]:
            return -1
        while i < self.N:
            i <<= 1
            if self.tree[i] < k:
                k -= self.tree[i]
                i |= 1
        return i - self.N

reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ord_p = [0] * n
ord_q = [0] * n

st = SegmTree([1] * n)
for i, val in enumerate(p):
    ord_p[i] = st.get_sum(0, val)
    st.add(val, -1)

st = SegmTree([1] * n)
for i, val in enumerate(q):
    ord_q[i] = st.get_sum(0, val)
    st.add(val, -1)

transfer = 0
for i in range(n-1, -1, -1):
    radix = n-i
    ord_p[i] = ord_p[i] + ord_q[i] + transfer
    if ord_p[i] < radix:
        transfer = 0
    else:
        transfer = 1
        ord_p[i] -= radix

st = SegmTree([1] * n)
for i in range(n):
    k = ord_p[i] + 1
    ord_q[i] = st.find_kth_nonzero(k)
    st.add(ord_q[i], -1)

print(*ord_q)