class Solution:
     def generateParenthesis(self, n):
         """
         :type n: int
         :rtype: List[str]
         """
         if n == 0:
             return []
         left = right = n
         result = []
         self.generate(left, right, result, '')
         return result
     def generate(self, left, right, result, string):
         if left == 0 and right == 0:
             result.append(string)
             return
         if left:
             self.generate(left - 1, right , result, string+'(')
         if left < right:
             self.generate(left, right - 1, result, string+')')