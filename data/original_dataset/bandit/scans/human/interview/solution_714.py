n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] = [A[i], i+1]
A.sort()
for i in range(n//2):
    print(A[i][1], A[n-i-1][1])