from heapq import heappush, heappop
N = int(input())
A = [int(a) for a in input().split()]
for i in range(N):
    if A[i] < 0:
        k = i
        break
A = [0] + [0 if i < k else A[i] for i in range(N) if i != k]

ans = A.pop()
H = []
while N > 2:
    N //= 2
    for i in range(N):
        heappush(H, A.pop())
    ans += heappop(H)

print(ans)