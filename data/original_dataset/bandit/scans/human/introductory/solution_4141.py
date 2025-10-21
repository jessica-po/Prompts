n = int(input())
a = [int(x) for x in input().split()]

flag = True

for x in a:
    if x % 2 == 0:
        if x % 3 and x % 5:
            flag = False

if flag:
    print('APPROVED')
else:
    print('DENIED')