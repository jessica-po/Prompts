n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)

mn = max(b)
b.remove(mn)
mn += max(b)

if mn >= s:
    print("YES")
else:
    print("NO")