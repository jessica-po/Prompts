n = int(input())
a = list(map(int, input().split()))

ans = [1]
t = 1

for i in range(n - 1):
    if a[i + 1] / a[i] <= 2:
        t += 1

    else:
        t = 1

    ans.append(t)

print(max(ans))