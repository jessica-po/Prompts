N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    ans += B[A[i]-1]
    if(A[i] == A[i-1]+1 and i != 0):
        ans += C[A[i]-2]
print(ans)