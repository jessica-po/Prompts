class Solution:
    def __init__(self):
        self.n, self.k = list(map(int, input().split()))
        self.s = [input() for i in range(0, self.n)]
        self.state = [
            (119, 6),
            (36, 2),
            (93, 5),
            (109, 5),
            (46, 4),
            (107, 5),
            (123, 6),
            (37, 3),
            (127, 7),
            (111, 6),
        ]
        self.p = []
        self.dp = [[False for j in range(0, self.k + 1)] for i in range(0, self.n)]

    def solve(self):
        for a in self.s:
            state = int(a[::-1], 2)
            stick = a.count("1")
            v = []
            for i, (dState, dStick) in enumerate(self.state):
                if dState & state == state:
                    v.append((i, dStick - stick))
            self.p.append(v)

        for i in range(self.n - 1, -1, -1):
            for j, stick in self.p[i]:
                if i == self.n - 1:
                    if stick <= self.k:
                        self.dp[i][stick] = True
                else:
                    for d in range(stick, self.k + 1):
                        self.dp[i][d] |= self.dp[i + 1][d - stick]
        if not self.dp[0][self.k]:
            return "-1"

        result = ""

        for i, v in enumerate(self.p):
            for j, stick in v[::-1]:
                ok = (self.k == stick) if i == self.n - 1 else (self.k >= stick and self.dp[i + 1][self.k - stick])
                if ok:
                    self.k -= stick
                    result += str(j)
                    break
        return result
            

print(Solution().solve())