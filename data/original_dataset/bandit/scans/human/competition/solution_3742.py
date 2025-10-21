import sys
readline = sys.stdin.readline

N = int(readline())
S = list(map(int, readline().split()))
S = [0 if s == 0 else 1 if s & 1 else -1 for s in S]

odd = -(-N//2)
even = N//2
for s in S:
    if s:
        if s == 1:
            odd -= 1
        else:
            even -= 1

inf = 10**9
dpe = [[inf]*(odd+1) for _ in range(even+1)]
dpo = [[inf]*(odd+1) for _ in range(even+1)]
dpe[0][0] = 0
dpo[0][0] = 0

for i in range(N):
    dp2e = [[inf]*(odd+1) for _ in range(even+1)]
    dp2o = [[inf]*(odd+1) for _ in range(even+1)]
    s = S[i]
    for e in range(even+1):
        for o in range(odd+1):
            if s == 1:
                dp2o[e][o] = min(dp2o[e][o], dpo[e][o], 1+dpe[e][o])
            elif s == -1:
                dp2e[e][o] = min(dp2e[e][o], dpe[e][o], 1+dpo[e][o])
            else:
                if o < odd:
                    dp2o[e][o+1] = min(dp2o[e][o+1], dpo[e][o], 1+dpe[e][o])
                if e < even:
                    dp2e[e+1][o] = min(dp2e[e+1][o], dpe[e][o], 1+dpo[e][o])
    dpe = [d[:] for d in dp2e]
    dpo = [d[:] for d in dp2o]

print(min(dpe[even][odd], dpo[even][odd]))