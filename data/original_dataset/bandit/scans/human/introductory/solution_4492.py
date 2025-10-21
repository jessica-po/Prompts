N, x = [int(n) for n in input().split(" ")]
A = [int(a) for a in input().split(" ")]

cnt = 0
if A[0] > x:
  cnt += A[0] - x
  A[0] = x

for i in range(1, len(A)):
  if A[i] + A[i - 1] > x:
    cnt += A[i] + A[i - 1] - x
    A[i] = x - A[i - 1]

print(cnt)