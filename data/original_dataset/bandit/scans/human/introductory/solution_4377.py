A = list(map(int, input().split()))
A.sort()
print(A[3] - A[0], A[3] - A[2], A[3] - A[1])