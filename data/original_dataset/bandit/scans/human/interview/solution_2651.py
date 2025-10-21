x,y=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A,B=sorted(A)[::-1],sorted(B)[::-1]
mod=10**9+7
X,Y=0,0
for i in range(x):
  d=A[i]*(x-i)-A[i]*(i)-A[i]
  X+=d
  X%=mod
for i in range(y):
  d=B[i]*(y-i)-B[i]*(i)-B[i]
  Y+=d
  Y%=mod
print(X*Y%mod)