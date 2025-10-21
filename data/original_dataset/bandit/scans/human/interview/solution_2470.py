import bisect
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(set(B))

        @lru_cache(None)
        def find_larger_value_in_B(val):
            if val >= B[-1]:
                return float('inf')
            return B[bisect.bisect_right(B, val)]

        @lru_cache(None)
        def min_last_value_given_operations(n, ops):
            if ops < 0:
                return float('inf')
            elif n == 0:
                return float('-inf')
            elif ops > n:
                return min_last_value_given_operations(n, n)

            prev_with_op = min_last_value_given_operations(n - 1, ops - 1)
            b = find_larger_value_in_B(prev_with_op)
            # dp(n - 1, ops) <= dp(n - 1, ops - 1)
            # if dp(n - 1, ops - 1) < A[n - 1] => dp(n - 1, ops) < A[n - 1]
            if prev_with_op < A[n - 1]:
                return min(A[n - 1], b)
            elif b <= A[n - 1]:
                return b
            elif min_last_value_given_operations(n - 1, ops) < A[n - 1]:
                return A[n - 1]
            return b

        last_success = -1
        for ops in range(min(len(A), len(B)), -1, -1):
            if min_last_value_given_operations(len(A), ops) == float('inf'):
                break
            last_success = ops

        return last_success