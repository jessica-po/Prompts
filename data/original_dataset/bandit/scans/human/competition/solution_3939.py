import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    if K not in A:
        print("no")
        continue
    
    if N == 1 or (A[0] >= K and A[1] >= K):
        print("yes")
        continue
    
    for i in range(2, N):
        if A[i] >= K and (A[i-1] >= K or A[i-2] >= K):
            print("yes")
            break
    else:
        print("no")
        continue