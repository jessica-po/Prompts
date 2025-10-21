import sys
input = lambda: sys.stdin.readline().rstrip()

ANS = []
T = int(input())
for _ in range(T):
    N, Q = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    ans = sum(max(b - a, 0) for a, b in zip([0] + A, A))
    ANS.append(ans)
    for _ in range(Q):
        l, r = list(map(int, input().split()))
        l, r = l-1, r-1
        if l == r:
            ANS.append(ans)
            continue
        
        ans -= max(A[l] - A[l-1], 0) if l else A[l]
        if l < N - 1: ans -= max(A[l+1] - A[l], 0)
        if r > l + 1: ans -= max(A[r] - A[r-1], 0)
        if r < N - 1: ans -= max(A[r+1] - A[r], 0)
        
        A[l], A[r] = A[r], A[l]
        
        ans += max(A[l] - A[l-1], 0) if l else A[l]
        if l < N - 1: ans += max(A[l+1] - A[l], 0)
        if r > l + 1: ans += max(A[r] - A[r-1], 0)
        if r < N - 1: ans += max(A[r+1] - A[r], 0)
        
        ANS.append(ans)

print("\n".join(map(str, ANS)))