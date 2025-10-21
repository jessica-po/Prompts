# import numpy as np
# import sys

# q=int(input())
mod=1000000007
dp=[(0,0),(0,0)]
for i in range(2,2000001):
	dp.append(((max(dp[-1])+2*max(dp[-2]))%mod,(dp[-1][0]+2*dp[-2][0]+1)%mod))
for o in range(int(input())):
	print(max(dp[int(input())-1])*4%mod)