u, v = list(map(int, input().split()))
if v < u or (v - u) % 2 != 0:
    print(-1)
else:
    if u == v:
        if u == 0:
            print(0)
        else:
            print("1\n" + str(u))
    else:
        w = (v - u) // 2
        if (w | u) == (w + u):
            print("2\n" + str(w|u) + ' ' + str(w))
        else:
            print("3\n" + str(u) + ' ' + str(w) + ' ' + str(w))