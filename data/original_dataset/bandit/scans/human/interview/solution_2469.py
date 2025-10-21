class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         if nums == []:
             return []
         
         dct = {}
         for el in nums:
             if el in dct:
                 dct[el] += 1
             else:
                 dct[el] = 1
             
         fin = []
         for key in dct:
             if dct[key] > (len(nums) // 3):
                 fin.append(key)
         
         return fin