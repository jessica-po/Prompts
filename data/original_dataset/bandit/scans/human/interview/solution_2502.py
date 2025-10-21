import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

# 適当な素数と原始根でrolling hash
MOD = 10 ** 9 + 993
base = 123450

S = np.array([ord(x) for x in input().rstrip()],dtype=np.int64)
T = np.array([ord(x) for x in input().rstrip()],dtype=np.int64)

# Sの方が長くする
LS = len(S)
LT = len(T)
n = (LT + (-LT) % LS) // LS
S = np.concatenate([S]*(n+1))
S = S[:LS+LT]

def cumprod(arr):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2); arr = arr.reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

base_inv = pow(base,MOD-2,MOD)
x = np.full(LS+LT,base,dtype=np.int64)
x[0] = 1
power = cumprod(x)
x = np.full(LS+LT,base_inv,dtype=np.int64)
x[0] = 1
power_inv = cumprod(x)

def to_rolling_hash(S):
    return (S * power[:len(S)] % MOD).cumsum() % MOD

S_hash = to_rolling_hash(S)
T_hash = to_rolling_hash(T)[-1] # 文字列全体

S_hash_LT = S_hash[LT-1:]
S_hash_LT[1:] -= S_hash.copy()[:LS]
S_hash_LT %= MOD
S_hash_LT *= power_inv[:LS+1]
S_hash_LT %= MOD

INF = 10 ** 18
visited = [False] * LS
dist = [INF] * LS # 操作終了位置からの距離

q = np.where(S_hash_LT[:LS] != T_hash)[0].tolist()

d = 0
while q:
    qq = []
    for x in q:
        if dist[x] == INF:
            dist[x] = d
            qq.append((x-LT)%LS)
    d += 1
    q = qq

answer = max(dist)
if answer >= INF:
    answer = -1

print(answer)