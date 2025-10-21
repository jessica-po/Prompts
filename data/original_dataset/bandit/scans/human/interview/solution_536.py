from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
if m < n - 1: stdout.write('-1')
elif m == n - 1: stdout.write('0' + '10' * m)
elif m == n: stdout.write('10' * m)
elif m == n + 1: stdout.write('10' * n + '1')
else:
    k = m - (n + 1)
    if k > n + 1: stdout.write('-1')
    elif k == n + 1: stdout.write('110' * n + '11')
    else: stdout.write('110' * k + '10' * (n - k) + '1')