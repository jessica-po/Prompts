x1, y1, x2, y2 = map(int, input().split())
#diagonal
if x1 != x2 and y1 != y2:
    if abs(x1 - x2) == abs(y1 - y2):
        print(x1, y2, x2, y1)
    else:
        print(-1)
#same side
elif x1 == x2:
    aux = abs(y2 - y1)
    print(x1 + aux, y1, x1 + aux, y2)
elif y1 == y2:
    aux = abs(x2 - x1)
    print(x1, y1 + aux, x2, y1 + aux)