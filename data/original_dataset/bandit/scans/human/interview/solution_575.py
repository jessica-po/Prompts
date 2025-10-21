n = int(input())
ax, ay = list(map(int, input().split(' ')))
bx, by = list(map(int, input().split(' ')))
cx, cy = list(map(int, input().split(' ')))

if ((cx < ax) == (bx < ax)) and ((cy < ay) == (by < ay)):
    print('YES')
else:
    print('NO')