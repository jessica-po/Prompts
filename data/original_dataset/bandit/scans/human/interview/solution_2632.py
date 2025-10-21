class Solution:
     def minPathSum(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         m, n = len(grid), len(grid[0])
         dp = [0] + [float('inf')] * (n-1)
         for i in range(m):
             dp[0] = dp[0] + grid[i][0]
             for j in range(1, n):
                 dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
         return dp[-1]