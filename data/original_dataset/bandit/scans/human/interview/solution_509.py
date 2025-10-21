import getpass
import sys


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()

n = ria()[0]
ar = []
for i in range(n):
    ar.append(ria()[0])

sm = sum(ar) / 2
for i in range(2 ** n):
    c = 0
    for j in range(n):
        if i & (1 << j):
            c += ar[j]
        else:
            c -= ar[j]
    if c % 360 == 0:
        print('YES')
        return
print('NO')