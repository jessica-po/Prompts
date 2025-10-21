from itertools import *


k, p = list(map(int, input().split()))
ss = 0
for i in range(1, k + 1):
    s = str(i)
    num = int(s + ''.join(reversed(s)))
    ss += num
    ss %= p
print(ss)