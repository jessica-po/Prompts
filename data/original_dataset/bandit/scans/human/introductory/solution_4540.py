N=int(input())
A=list(map(int,input().split()))

SUM=abs(A[0])
for i in range(N):
  if i < N-1:
    SUM += abs(A[i+1]-A[i])
  else:
    SUM += abs(0-A[i])

now=0
for i in range(N):
  if i != N-1:
    diff = abs(A[i+1]-now)-abs(A[i]-now)-abs(A[i+1]-A[i])
    now = A[i]
  else:
    diff = abs(0-now)-abs(A[i]-now)-abs(0-A[i])
  print(SUM + diff)