import numpy as np
from numba import njit
R,C,K=list(map(int,input().split()))
vl=np.zeros((R,C), np.int64)
for _ in range(K):
  r,c,v=list(map(int,input().split()))
  vl[r-1][c-1]=v
@njit
def main():
  dp=np.zeros((R+1,C+1,4), np.int64)
  for i in range(1,R+1):
    for j in range(1,C+1):
      for k in range(4):
        dp[i][j][k]=max(dp[i][j-1][k],dp[i-1][j][3])
      for k in range(3,0,-1):
        dp[i][j][k]=max(dp[i][j][k],dp[i][j][k-1]+vl[i-1][j-1])
  return dp[R][C][3]
print((main()))