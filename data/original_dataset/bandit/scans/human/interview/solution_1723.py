def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
if n < 6:
    print(-1)
else:
    t = ['1 2', '1 3', '1 4', '2 5', '2 6']
    for i in range(7, n + 1):
        t.append('1 ' + str(i))
    print('\n'.join(t))
t = []
for i in range(2, n + 1):
    t.append('1 ' + str(i))
print('\n'.join(t))