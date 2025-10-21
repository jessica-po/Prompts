n, k = map(int, input().split())
s = input()

left = k - 1
right = n - k
if left < right:
    print('LEFT\n' * left, end = '')
    for i in range(len(s) - 1):
        c = s[i]
        print('PRINT', c)
        print('RIGHT')
    print('PRINT', s[-1])
else:
    print('RIGHT\n' * right, end = '')
    for i in range(len(s) - 1):
        c = s[-i - 1]
        print('PRINT', c)
        print('LEFT')
    print('PRINT', s[0])