Q = int(input())
qs = [input().split() for i in range(Q)]

import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign

    def size(self):
        return len(self.hq)

lq = Heapq([], True)
rq = Heapq([], False)

ofs = 0
for q in qs:
    if q[0] == '2':
        print(lq.top(), ofs)
        continue
    _,a,b, = q
    a,b = int(a),int(b)
    ofs += b
    lq.push(a)
    rq.push(a)
    if lq.top() > rq.top():
        l,r = lq.pop(), rq.pop()
        ofs += abs(l-r)
        lq.push(r)
        rq.push(l)