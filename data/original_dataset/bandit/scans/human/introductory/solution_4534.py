class Solution:
     def getRow(self, k):
         """
         :type k: int
         :rtype: List[int]
         """
         res = [1]
         cur = k
         for i in range(k//2):
             res += res[-1] * cur // (i+1),
             cur -= 1
         if k % 2 == 0:
             res = res + res[:-1][::-1]
         else:
             res = res + res[::-1]
         return res