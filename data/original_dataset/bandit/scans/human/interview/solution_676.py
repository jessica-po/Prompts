n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = sorted(a)
#print(a)
if n == 0:
    print('YES')
    print(1)
    print(1)
    print(3)
    print(3)
elif n == 1:
    print('YES')
    print(a[0])
    print(3 * a[0])
    print(3 * a[0])
elif n == 2:
    if a[0] * 3 >= a[1]:
        print('YES')
        print(a[0] * 3)
        print(a[0] * 4 - a[1])
    elif a[1] % 3 == 0 and a[1] // 3 <= a[0]:
        print('YES')
        print(a[1] // 3)
        print(a[1] + a[1] // 3 - a[0])
    elif (a[0] + a[1]) % 4 == 0 and (a[0] + a[1]) // 4 <= a[0]:
        print('YES')
        print((a[0] + a[1]) // 4)
        print(3 * ((a[0] + a[1]) // 4))
    else:
        print('NO')
elif n == 3:
    if a[0] * 3 >= a[2] and 4 * a[0] == a[1] + a[2]:
        print('YES')
        print(a[0] * 3)
    elif a[2] % 3 == 0 and a[2] // 3 <= a[0] and a[2] + a[2] // 3 == a[0] + a[1]:
        print('YES')
        print(a[2] // 3)
    elif a[2] == a[0] * 3:
        print('YES')
        print(4 * a[0] - a[1])
    else:
        print('NO')
elif n == 4:
    if a[3] == 3 * a[0] and a[0] + a[3] == a[1] + a[2]:
        print('YES')
    else:
        print('NO')