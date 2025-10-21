a, b = list(map(int, input().split()))
s = input()
sm = [[0, 0] for i in range(len(s))]
repl = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
for i, c in enumerate(s):
    sm[i][0] = sm[i - 1][0] + repl[c][0]
    sm[i][1] = sm[i - 1][1] + repl[c][1]
# a = n * sm[-1][0] + sm[i][0]
for i in range(len(s)):
    na, nb = 0 if sm[-1][0] == 0 else (a - sm[i][0]) // sm[-1][0], 0 if sm[-1][1] == 0 else (b - sm[i][1]) // sm[-1][1]
    if a == na * sm[-1][0] + sm[i][0] and b == nb * sm[-1][1] + sm[i][1] and (0 in sm[-1] or na == nb) and na >= -1 and nb >= -1:
        print('Yes')
        return
print('No')