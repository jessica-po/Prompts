cols = int(input())
nums = [int(i) for i in input().split()]

nums = sorted(nums)
out = ""
for num in nums: out=out+str(num)+" "
print(out[:-1])