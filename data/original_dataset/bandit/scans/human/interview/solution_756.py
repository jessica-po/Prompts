n = int(input())
a = list(map(int, input().split()))

cutoff = 15
for x in a:
    if x > cutoff:
        break
    cutoff = x + 15

print(min(90, cutoff))