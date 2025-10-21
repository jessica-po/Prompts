class Solution:
     def searchRange(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
         start = self.firstGreaterEqaul(nums, target)
         if start==len(nums) or nums[start]!=target:
             return [-1, -1]
         return [start, self.firstGreaterEqaul(nums, target+1)-1]
     def firstGreaterEqaul(self, nums, target):
         lo, hi = 0, len(nums)
         while lo<hi:
             mid = (hi+lo)//2
             if nums[mid]<target:
                 lo = mid + 1
             else:
                 hi = mid
         return lo