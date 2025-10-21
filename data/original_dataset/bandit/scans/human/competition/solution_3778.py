import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

Ans = []
one = []
tt = []
for i in range(N-1, -1, -1):
    a = A[i]
    if a == 0:
        continue
    if a == 1:
        Ans.append((i, i))
        one.append((i, i))
        continue
    if a == 2:
        if not one:
            Ans = None
            break
        else:
            oi, _ = one.pop()
            Ans.append((oi, i))
            tt.append((oi, i))
            continue
    else:
        if not tt:
            if not one:
                Ans = None
                break
            else:
                oi, wi = one.pop()
                Ans.append((i, wi))
                Ans.append((i, i))
                tt.append((i, i))
        else:
            oi, wi = tt.pop()
            Ans.append((i, wi))
            Ans.append((i, i))
            tt.append((i, i))
        continue

if Ans is None:
    print(-1)
else:
    print(len(Ans))
    if Ans:
        print('\n'.join(f'{a+1} {b+1}' for a, b in Ans))