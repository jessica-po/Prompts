n = int(input())
A = list(map(int, input().split()))
A.sort()
A[0], A[-1] = A[-1], A[0]
print(" ".join(list(map(str, A))))