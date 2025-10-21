n = int(input())
x = list(map(int, input().split()))
d = None
s = 1
c = x[0]
for i in range(1, n):
    if x[i] == c:
        s += 1
    else:
        if d is None:
            d = s
        else:
            if (s != d):
                print("NO")
                break
        s = 1
        c = x[i]
else:
    if (d is None) or (s == d):
        print("YES")
    else:
        print("NO")