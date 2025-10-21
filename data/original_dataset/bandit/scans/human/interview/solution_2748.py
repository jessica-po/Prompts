class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         
         def dfs(digits, current, result):
             if not digits:
                 result.append(current)
                 return
             for c in dic[digits[0]]:
                 dfs(digits[1:], current + c, result)
         
         
         if not digits:
             return []
         
         dic = { '2' : "abc", '3': "def", '4':"ghi", 
                '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv",'9': "wxyz" }
         result = []
         dfs(digits, "", result)
         return result