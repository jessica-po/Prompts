class Solution:
     def minimumTotal(self, triangle):
         """
         :type triangle: List[List[int]]
         :rtype: int
         """
         length = len(triangle)
         for i in range(length - 1, 0, -1):
             for j in range(1, len(triangle[i])):
                 if triangle[i][j] < triangle[i][j-1]:
                     triangle[i-1][j-1] += triangle[i][j]
                 else:
                     triangle[i-1][j-1] += triangle[i][j - 1]
         return triangle[0][0]