import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None]*T
for qu in range(T):
    N, K = map(int, readline().split())
    S = list(map(lambda x: ord(x)-97, readline().strip()))
    S.sort()
    if len(set(S[:K])) != 1:
        Ans[qu] = chr(97+S[K-1])
        continue
    L = len(set(S[K:]))
    if L == 1:
        res = [S[0]] + [S[K]]*(-((K-N)//K))
    else:
        res = [S[0]] + S[K:]
    Ans[qu] = ''.join(map(lambda x: chr(x+97), res))
            
print('\n'.join(map(str, Ans)))