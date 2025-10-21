import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

from heapq import heappop, heappush, heapify
from collections import deque
class SWAG_Stack():
    def __init__(self, F):
        self.stack1 = deque()
        self.stack2 = deque()
        self.F = F
        self.len = 0

    def push(self, x):
        if self.stack2:
            self.stack2.append((x, self.F(self.stack2[-1][1], x)))
        else:
            self.stack2.append((x, x))
        self.len += 1

    def pop(self):
        if not self.stack1:
            while self.stack2:
                x, _ = self.stack2.pop()
                if self.stack1:
                    self.stack1.appendleft((x, self.F(x, self.stack1[0][1])))
                else:
                    self.stack1.appendleft((x, x))
        x, _ = self.stack1.popleft()
        self.len -= 1
        return x

    def sum_all(self):
        if self.stack1 and self.stack2:
            return self.F(self.stack1[0][1], self.stack2[-1][1])
        elif self.stack1:
            return self.stack1[0][1]
        elif self.stack2:
            return self.stack2[-1][1]
        else:
            return float("inf")

n,p = map(int, input().split())
t = list((j, i) for i,j in enumerate(map(int, input().split())))
heapify(t)

stack = SWAG_Stack(min)

heap = []
cur = 0
ans = [-1]*n
hoge = 0
# 今追加できるやつで最も小さいものを追加
# ここでなにもなかったら？
#   時間を変更する
# 次の時間までに追加できるものを追加
# 清算
while hoge != n:
    if heap and stack.sum_all() > heap[0]:
        j = heappop(heap)
        stack.push(j)

    if stack.len==0 and t:
        cur = max(cur, t[0][0])

    while t and t[0][0] <= cur+p:
        ti, i = heappop(t)
        if ti == cur+p:
            # 後回し
            heappush(heap, i)
        else:
            # いま追加できるか確認
            if stack.sum_all() > i:
                stack.push(i)
            else:
                # 後回し
                heappush(heap, i)

    if stack.len:
        j = stack.pop()
        cur += p
        ans[j] = cur
        hoge += 1
print(*ans)