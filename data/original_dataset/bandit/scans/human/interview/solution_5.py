n, pos, l, r = map(int, input().split())

if l > 1 and r < n:
    if l <= pos and pos <= r:
        if pos - l < r - pos:
            print(pos - l + 1 + r - l + 1)
        else:
            print(r - pos + 1 + r - l + 1)
    elif pos > r:
        print(pos - r + 1 + r - l + 1)
    else:
        print(l - pos + 1 + r - l + 1)
elif l == 1 and r < n:
    print(int(abs(pos - r)) + 1)
elif l > 1 and r == n:
    print(int(abs(pos - l)) + 1)
else:
    print(0)