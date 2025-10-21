import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from bisect import bisect_left


n, k = getList()
nums = getList()
nums.sort()
half = (n // 2) + 1
nums = nums[half-1:]
sm = sum(nums)

def check(arr, k, tgt):
    for num in arr:
        sub = max(0, (tgt - num))
        if sub == 0:
            return True
        k -= sub
        if k < 0:
            return False

    return True


mn = 0
mx = 3 * (10 ** 9)
# print(nums, sm)
while(mx-mn > 1):
    md = (mx+mn) // 2
    # print(md)
    if check(nums, k, md):
        mn = md
    else:
        mx = md

if not check(nums, k, md):
    md -= 1
print(md)