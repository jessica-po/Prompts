class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        
        i = 0
        while A[i] < 0 and K > 0:
            A[i] *= -1
            i += 1
            K -= 1
            
        if K % 2 == 1 and 0 not in A:
            return sum(A) - 2*min(A)
        return sum(A)