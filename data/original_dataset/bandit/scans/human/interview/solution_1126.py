import sys
import numpy as np
import math
import collections
import copy
import decimal
from collections import deque 
from functools import reduce
from itertools import product
from itertools import combinations
N, X, M = list(map(int, input().split()))

# X^2がMより大きい場合はMで割った余り、小さければそのままを返却
def f(X, M):
    if X**2 >= M:
        return X**2 % M
    else:
        return X**2

appear = np.full(M, -1)
seq = []
fx = X
appear[fx] = 0
seq.append(fx)
for i in range(1, N):
    fx = f(fx, M)
#     print(fx, appear[fx])
    if appear[fx] != -1:
        loop_st = appear[fx]
        loop_en = i
        break
    seq.append(fx)
    appear[fx] = i
seq.insert(0, 0)
seq_sum = np.cumsum(seq)

if N <= len(seq)-1 :
    print((seq_sum[N]))
else:
    # ループの前まで
    lp_b = seq_sum[loop_st-1]
    # ループしている個数を求める
    loop_num = (len(seq_sum)-1) - loop_st
    # 商はループ回数、余りはループしきらなかった分
    qu = (N-(loop_st)) // loop_num
    mo = (N-(loop_st)) % loop_num
    # ループした分だけかける
    lp_sum = (seq_sum[-1] - seq_sum[loop_st]) * qu
    # 最後の余りの部分を加算
    lp_en = seq_sum[loop_st+mo] - seq_sum[loop_st-1]
    print((lp_b+lp_sum+lp_en))