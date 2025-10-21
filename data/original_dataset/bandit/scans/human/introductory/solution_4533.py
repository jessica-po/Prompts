class Solution:
     def findContentChildren(self, g, s):
         """
         :type g: List[int]
         :type s: List[int]
         :rtype: int
         """
         res = 0
         heapq.heapify(g)
         s.sort()
         for num in s:
             if not g:
                 break
             elif g[0] <= num:
                 res += 1
                 heapq.heappop(g)
         return res