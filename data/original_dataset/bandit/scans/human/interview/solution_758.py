n, b = input(), input().replace('R', '0').replace('B', '1')
print(int(b[:: -1], 2))