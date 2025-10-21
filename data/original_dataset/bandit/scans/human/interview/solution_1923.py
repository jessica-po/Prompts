N=int(input())
A=list(map(int,input().split()))
A.sort()
sm=0
for i in range(0,2*N,2):
  sm+=A[i]
print(sm)