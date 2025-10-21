def create_list(n, num_of_calls):
    if n == 1:
        return [1], 0
    if n == 2:
        return [2, 1], 2
    if num_of_calls == 2:
        return list(range(2, n // 2 + 2)) + [1] +\
               list(range(n // 2 + 2, n + 1)), 2

    list1, num_of_calls1 = create_list(n // 2, num_of_calls - 2)
    if num_of_calls1 == num_of_calls - 2:
        return list1 + list(range(n // 2 + 1, n + 1)), num_of_calls

    list2, num_of_calls2 = create_list((n + 1) // 2,
                                       num_of_calls - num_of_calls1 - 2)
    return list1 + [x + n // 2 for x in list2], \
        num_of_calls1 + num_of_calls2 + 2


def main():
    n, k = [int(x) for x in input().split()]
    if k % 2 != 1:
        print(-1)
        return

    if k == 1:
        print(' '.join([str(x) for x in range(1, n + 1)]))
        return

    num_list, num_of_calls = create_list(n, k - 1)
    if num_of_calls != k - 1:
        print(-1)
        return
    print(' '.join([str(x) for x in num_list]))


def __starting_point():
    main()

__starting_point()