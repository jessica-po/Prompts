import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    B = [A[i+K]-A[K] for i in range(N-K)]
    mi = 10**20
    mx = -1
    for i in range(N-K):
        if A[i+K]-A[i] < mi:
            mi = A[i+K]-A[i]
            mx = (A[i+K]+A[i]) // 2
    
    print(mx)