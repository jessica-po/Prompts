N, C = list(map(int, input().split()))
Nums = list(map(int, input().split()))
Max = 0
for i in range(N - 1):
    Max = max(Max, Nums[i] - Nums[i + 1] - C)
print(Max)