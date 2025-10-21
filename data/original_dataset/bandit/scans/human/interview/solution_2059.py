n = int(input())
nums = [int(x) for x in input().split()]
ans = 10 ** 12
for idx, num in enumerate(nums):
    dist = max(idx, n - idx - 1)
    curr = num // dist
    ans = min(ans, curr)
print(ans)