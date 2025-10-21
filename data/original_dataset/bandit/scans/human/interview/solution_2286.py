from sys import stdout

n = int(input())


class Person:

    num = n - 1

    def __init__(self, rel):
        self.relationship = int(rel, 2)

    def __getitem__(self, k):
        return (self.relationship >> Person.num - k) & 1


rel = [Person(input()) for _ in range(n)]

dp = [[0] * n for _ in range(1 << n)]

for people in range(1, 1 << n):
    ones = [i for i in range(n) if people & (1 << i)]
    # print(f'ones: {ones}')
    one_num = len(ones)

    if one_num == 1:
        dp[people][ones[0]] = [1]
        continue

    for i in ones:
        dp[people][i] = [0] * (1 << one_num - 1)
        pre_people = people ^ (1 << i)
        for j in ones:
            if j == i:
                continue
            for pre_s, times in enumerate(dp[pre_people][j]):
                s = pre_s | (rel[j][i] << one_num - 2)
                # print(f'dp[{people}][{i}][{s}]: {dp[people][i][s]}')
                dp[people][i][s] += times

people = (1 << n) - 1

for s in range(1 << (n-1)):
    ans = 0
    for i in range(n):
        ans += dp[people][i][s]
    print(ans, end=' ')