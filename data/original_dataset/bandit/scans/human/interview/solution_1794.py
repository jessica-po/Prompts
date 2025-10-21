MAX_N = 100000

def maxi(a, b):
    if a[0] > b[0]:
        return a
    else:
        return b

class Segment_Tree:
    def init(self, left, right, data, leftbound, rightbound):
        self.data = data
        self.left = left
        self.right = right
        self.leftbound = leftbound
        self.rightbound = rightbound
        return self
    def build(self, a, leftbound, rightbound):
        #print(leftbound, rightbound, a)
        if len(a) == 0:
            return self.init(-1, -1, [0, -1], MAX_N + 1, -1)
        elif len(a) == 1:
            return self.init(-1, -1, a[0], leftbound, rightbound)
        else:
            middle = (leftbound + rightbound) // 2
            self.left = Segment_Tree()
            self.right = Segment_Tree()
            return self.init(self.left.build(a[:middle - leftbound], leftbound, middle), self.right.build(a[middle - leftbound:], middle, rightbound), maxi(self.left.data, self.right.data), leftbound, rightbound)
    def get(self, l, r):
        if l <= self.leftbound and r >= self.rightbound:
            return self.data
        elif l < self.left.rightbound and r > self.right.leftbound:
            return maxi(self.left.get(l, r), self.right.get(l, r))
        elif l >= self.right.leftbound:
            return self.right.get(l, r)
        else:
            return self.left.get(l, r)
            
n = int(input())
a = list(map(int, input().split())) + [n]
a = [[a[i] - 1, i] for i in range(n)]
Tree = Segment_Tree()
Tree.build(a, 0, n)
dp = [0] * n
ans = 0
for i in range(n - 2, -1, -1):
    m = Tree.get(i + 1, a[i][0] + 1)[1]
    dp[i] = dp[m] - (a[i][0] - m) + n - i - 1;
    ans += dp[i]
print(ans)