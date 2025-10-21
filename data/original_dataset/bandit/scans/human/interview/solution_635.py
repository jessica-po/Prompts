# map(int, input().split())
# list(map(int, input().split()))
n, m = list(map(int, input().split()))
m -= 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] == 0:
    print("NO")
    return
elif a[m] == 1:
    print("YES")
    return
elif b[m] == 0:
    print("NO")
    return
else:
    for i in range(m, n):
        if a[i] and b[i]:
            print("YES")
            return
    print("NO")