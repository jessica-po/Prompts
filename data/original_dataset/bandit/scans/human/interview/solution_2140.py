s = list(input())
n = len(s) // 2
m = int(input())
a = [int(x) for x in input().split()]
sums = [0] * (n + 1)
for i in a:
    sums[i - 1] += 1
for i in range(1, len(sums)):
    sums[i] += sums[i-1]

for i in range(n):
    if (sums[i] % 2 == 1):
        s[i], s[-i-1] = s[-i-1], s[i]

print("".join(s))