n = int(input())
num = list(map(int, input().split()))
for i in range(n - 1):
    if i % 2 == 0:
        num.pop(num.index(max(num)))
    else:
        num.pop(num.index(min(num)))
print(*num)