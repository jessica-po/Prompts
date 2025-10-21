rgb = list(map(int, input().split()))

l = ''.join(str(n) for n in rgb)
if int(l)%4 == 0:
    print('YES')
else:
    print('NO')