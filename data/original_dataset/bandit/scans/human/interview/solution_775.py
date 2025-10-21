from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
position = set(list(map(int, stdin.readline().split())))

start = 1
for i in range(k):
    if start in position:
        break
    else:
        a, b = map(int, stdin.readline().split())
        if a == start:
            start = b
        elif b == start:
            start = a

stdout.write(str(start))