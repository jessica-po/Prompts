x = int(input())
if x <= 6:
    print((1))
    return
elif 7 < x <= 11:
    print((2))
    return
else:
    n = x//11
    if x - n*11 == 0:
        print((2*n))
        return
    elif x - n*11 <= 6:
        print((2*n+1))
    else:
        print((2*n+2))