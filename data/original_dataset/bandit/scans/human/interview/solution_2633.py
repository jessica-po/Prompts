class Solution:
     def calculateMinimumHP(self, dungeon):
         """
         :type dungeon: List[List[int]]
         :rtype: int
         """
         '''
         逆回，当是小于等于0时，是相反数+1.   dp为到当前i,j只要需要的点数， 最小为1，保证 活着
         
         r,  c   r   ,c+1
         r+1,c   r+1,c+1
         
         r,c处至少的点数 - r,c处惩罚点数  是  其下面和右面最少需要的点数，  也就是第33行
         
         '''
         row = len(dungeon)
         col = len(dungeon[0])
         dp = [[0 for  c in range(col)] for r in range(row)]
         if dungeon[-1][-1] <= 0:
             dp[-1][-1] = -dungeon[-1][-1] + 1
         else:
             dp[-1][-1] = 1
         for r in range(row-2,-1,-1):
             dp[r][-1] = dp[r+1][-1]  - dungeon[r][-1]
             if dp[r][-1] <= 0:
                 dp[r][-1] = 1
         for c in range(col-2,-1,-1):
             dp[-1][c] = dp[-1][c+1]  - dungeon[-1][c]
             if dp[-1][c] <= 0:
                 dp[-1][c] = 1
         for r in range(row-2,-1,-1):
             for c in range(col-2,-1,-1):
                 dp[r][c] = min(dp[r+1][c],dp[r][c+1]) - dungeon[r][c]
                 if dp[r][c] <= 0:
                     dp[r][c] = 1
         return dp[0][0]