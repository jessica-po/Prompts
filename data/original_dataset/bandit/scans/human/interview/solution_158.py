n = int(input())
z = list(map(int, input().split()))
z.sort()
if z[n - 1] < z[n]:
    print("YES")
else:
    print("NO")