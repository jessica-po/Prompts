n = int(input())
s = list([1 if x == '>' else -1 for x in input().strip()])
d = list(map(int, input().strip().split()))
b = [False for _ in range(n)]

c = 0
while True:
    c += s[c] * d[c]
    if c >= n or c < 0:
        print('FINITE')
        return
    if b[c]:
        print('INFINITE')
        return
    b[c] = True