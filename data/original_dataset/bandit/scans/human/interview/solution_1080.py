import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from bisect import bisect_left

n = getN()
nums = getList()

if sum(nums) % 2 == 1:
    print("NO")
    return

if max(nums) * 2 > sum(nums):
    print("NO")
    return

print("YES")