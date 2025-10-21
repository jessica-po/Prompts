import sys
input = sys.stdin.readline
from bisect import bisect_right as br
P = 10**9+7
N = int(input())
X = []
maxinn = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    maxinn = max(maxinn, b)
    X.append((a, b))
X = sorted(X)
OUT = [0]
VOL = [0]
CNT = [1]

for out, inn in X:
    i = br(OUT, inn) - 1
    vol = VOL[i] + out - inn
    if OUT[-1] != out:
        OUT.append(out)
        VOL.append(VOL[-1] if len(CNT)>1 else 0)
        CNT.append(CNT[-1] if len(CNT)>1 else 0)
    
    if VOL[-1] < vol:
        VOL[-1] = vol
        CNT[-1] = CNT[i]
    elif VOL[-1] == vol:
        CNT[-1] += CNT[i]
        CNT[-1] %= P

mi = min([OUT[i]-VOL[i] for i in range(len(CNT)) if OUT[i] > maxinn])
print(sum([CNT[i] for i in range(len(CNT)) if OUT[i] > maxinn and OUT[i]-VOL[i] == mi])%P)