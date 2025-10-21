class Solution:
     def subsets(self, nums):
         """
         :type nums: List[int]
         :rtype: List[List[int]]
         """
         subsets = [[]]
         for v in nums:
             extra = []
             for s in subsets:
                 extra.append(s+[v])
             subsets += extra
         return subsets