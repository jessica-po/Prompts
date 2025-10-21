A, B, C = list(map(int, input().split()))

g = min(A//3,B//2,C//2)

A -= g*3
B -= g*2
C -= g*2

L = [0,0,1,2,0,2,1]
def calc(today, x):
    if x[L[today]] == 0:
        return 0
    y = [xx for xx in x]
    y[L[today]] -= 1
    return calc((today+1)%7, y) + 1

ma = 0
for i in range(7):
    ma = max(ma, calc(i, [A,B,C]))

print(ma+g*7)