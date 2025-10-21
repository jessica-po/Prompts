3

def readln(): return tuple(map(int, input().split()))

n, = readln()
ans = []
for x, y in sorted([readln() for _ in range(n)], key=lambda x: abs(x[0]) + abs(x[1])):
    if x > 0:
        ans.append('1 %d R' % x)
    if x < 0:
        ans.append('1 %d L' % -x)
    if y > 0:
        ans.append('1 %d U' % y)
    if y < 0:
        ans.append('1 %d D' % -y)
    ans.append('2')
    if x > 0:
        ans.append('1 %d L' % x)
    if x < 0:
        ans.append('1 %d R' % -x)
    if y > 0:
        ans.append('1 %d D' % y)
    if y < 0:
        ans.append('1 %d U' % -y)
    ans.append('3')
print(len(ans))
print('\n'.join(ans))