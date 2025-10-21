import sys
readline = sys.stdin.readline

MOD = 998244353
N = int(readline())
wants = [tuple(map(int, readline().split()))[1:] for _ in range(N)]

Q = [0]*(10**6+1)
P = [0]*(10**6+1)

for i in range(N):
    k = len(wants[i])
    kinv = pow(k, MOD-2, MOD)
    for w in wants[i]:
        P[w] += 1
        Q[w] = (Q[w] + kinv)%MOD

res = 0
for i in range(10**6+1):
    res = (res+P[i]*Q[i])%MOD

print(pow(N**2, MOD-2, MOD)*res%MOD)