class Solution:
    def longestValidParentheses(self, s: str) -> int:
        memo ={}
        n =len(s)
        def dp(i):
            if i<=0:
                return 0
            if i in memo:
                return memo[i]
            if (s[i-1],s[i])==('(',')'):
                memo[i]=dp(i-2)+2
            elif (s[i-1],s[i])==(')',')') and i-dp(i-1)-1>=0 and s[i-dp(i-1)-1]=='(':
                memo[i]=dp(i-1)+2+dp(i-dp(i-1)-2)
            else:
                memo[i]=0
            return memo[i]
        ret = 0
        for i in range(n-1,0,-1):
            ret = max(ret, dp(i))
        return ret