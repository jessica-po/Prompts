def check(pali):
    for i in range(len(pali) // 2):
        if pali[i] != pali[-i - 1]:
            return False

    return True


def __starting_point():
    s = input()
    k = int(input())

    if len(s) % k != 0:
        print('NO')
        return

    step = len(s) // k
    for i in range(k):
        if not check(s[i * step: (i + 1) * step]):
            print('NO')
            return

    print('YES')
__starting_point()