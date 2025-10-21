n = int(input())
a = [int(x) for x in input().split()]
alive = 0
left = n
for i in range(n - 1, -1, -1):
    if i < left:
        alive += 1
    left = min(left, i - a[i])
print(alive)