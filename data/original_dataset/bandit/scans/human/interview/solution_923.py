n = int(input())
a = list(map(int, input().split()))
for i in range(n + 1):
    for j in range(n):
        if j % 2 == 0:
            a[j] = (a[j] + 1) % n
        else:
            a[j] = (a[j] - 1) % n
    for j in range(n):
        if a[j] != j:
            break
    else:
        print("Yes")
        return
print("No")