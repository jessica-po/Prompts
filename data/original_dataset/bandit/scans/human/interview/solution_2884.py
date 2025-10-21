class Solution:
     def combinationSum2(self, candidates, target):
                 
         def dfs(i, val, path):
             while i < len(candidates):
                 num = candidates[i]
                 val_ = val + num
                 path_ = path + [num]
                 if val_ > target:
                     return
                 elif val_ == target:
                     ans.append(path_)
                     return                  
                 dfs(i+1, val_, path_)
                 while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                     i += 1
                 i += 1
                
         candidates = sorted(candidates)
         ans = []
         dfs(0, 0, [])
         return ans