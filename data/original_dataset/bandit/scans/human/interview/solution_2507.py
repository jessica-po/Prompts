import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 二分探索
N, K = lr()
A = np.array(lr())
F = np.array(lr())
A.sort()
F = np.sort(F)[::-1]

def check(x):
    count = np.maximum(0, (A - (x // F))).sum()
    return count <= K

left = 10 ** 12 # 可能
right = -1 # 不可能
while left > right + 1:
    mid = (left+right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
# 51