def is_izi(k):
    i = 2
    while (i * i <= k):
        if (k % i == 0):
            return 0
        i += 1
    return 1
n = int(input())
if (is_izi(n)):
    print(1)
elif n % 2 == 0:
    print(2)
elif n % 2 == 1:
    if (is_izi(n - 2)):
        print(2)
    else:
        print(3)