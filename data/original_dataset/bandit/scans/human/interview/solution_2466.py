class Solution:
     def permute(self, nums):
         """
         :type nums: List[int]
         :rtype: List[List[int]]
         """
         all_permutes = []
         self.permute_nums(all_permutes, nums, [])
         return all_permutes
     
     def permute_nums(self, all_permutes, nums, cur_permute):
         if len(nums) == 0:
             all_permutes.append(cur_permute)
             return
 
         for i in range(len(nums)):
             num = nums[i]
 
             self.permute_nums(all_permutes, nums[0:i] + nums[i+1:len(nums)], cur_permute + [num])