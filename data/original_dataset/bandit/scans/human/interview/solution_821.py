s, v1, v2, t1, t2 = list(map(int, input().split()))
a1 = 2 * t1 + s * v1
a2 = 2 * t2 + s * v2
if a1 < a2:
    print('First')
elif a1 > a2:
    print('Second')
else:
    print('Friendship')