n = int(input())
a = list([int(x) - 1 for x in input().split()])

ans = False

for i in range(n):
    if a[a[a[i]]] == i:
        ans = True
        break

print('YES' if ans else 'NO')