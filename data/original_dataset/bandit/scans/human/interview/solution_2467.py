class Solution:
     def combinationSum3(self, k, n):
         """
         :type k: int
         :type n: int
         :rtype: List[List[int]]
         """
         to_return = []
         self.backtrack(to_return, [], k, n, 1)
         return to_return
     
     def backtrack(self, to_return, temp, k, n, start):
         total = sum(temp)
         
         if total > n:
             return
         if len(temp) == k and total == n:
             to_return.append(temp[:])
             return
         
         for i in range(start, 10):
             temp.append(i)
             self.backtrack(to_return, temp, k, n, i + 1)
             temp.pop()