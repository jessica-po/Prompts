n = int(input())
nums = (abs(int(x)) for x in input().split())
nums = list(sorted(nums))
left = 0
right = 0
ans = 0
while left < n:
    while right < n and nums[right] <= 2 * nums[left]:
        right += 1
    ans += right - left - 1
    left += 1
print(ans)