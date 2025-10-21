class Solution:
     def subsetsWithDup(self, nums):
         """
         :type nums: List[int]
         :rtype: List[List[int]]
         """
         def dfs(idx, path):
             subsets.append(path)
             
             for i in range(idx, len(nums)):
                 if i > idx and nums[i] == nums[i-1]:
                     continue
                 dfs(i + 1, path + [nums[i]])     
         nums.sort()
         subsets = []
         dfs(0, [])
         
         return subsets