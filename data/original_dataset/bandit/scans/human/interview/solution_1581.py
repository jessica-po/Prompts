import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N, K = lr()
M = int(N**.5)

# M+1以上で、Nを割るとxになるもの
upper_cnt = np.zeros(M+1, dtype=np.int64) # 1-indexed
A = np.arange(M+1, dtype=np.int64)
upper_cnt[1:] = N // A[1:] - np.maximum(M, N // (A[1:]+1)) # Mの時はlowerで数えるので0に

# 桁DP
lower = np.zeros(M+1, dtype=np.int64) # 1-indexed
upper = np.zeros(M+1, dtype=np.int64)
#最初は制限なしなので1を置いておく
lower[1] = 1
for i in range(K):
    prev_lower = lower.copy()
    prev_upper = upper.copy()
    lower_cum = prev_lower.cumsum() % MOD
    upper_cum = prev_upper.cumsum() % MOD
    # lower と upper から lower へ
    lower = np.zeros(M+1, dtype=np.int64)
    lower[1:] += (lower_cum[-1] + upper_cum[-1])
    lower[1:] -= upper_cum[:-1] # 大きすぎる値を引く
    # upper から upper はなし
    # lower から upper へ
    upper = lower_cum * upper_cnt
    lower %= MOD; upper %= MOD

answer = (lower[1:].sum() + upper[1:].sum()) % MOD
print(answer)