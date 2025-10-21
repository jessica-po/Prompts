#!/usr/bin/env python3


class CantException(Exception):
    pass


def odd_v(value):
    return 1 if value % 2 == 1 else -1


change_idx = 1

acceptable = {-1: set(), 1: set()}


def change(card_values, oddv, m):
    nonlocal change_idx

    if acceptable[oddv]:
        res = acceptable[oddv].pop()
        card_values.add(res)
        return res

    change_idx_start = change_idx

    while change_idx in card_values or odd_v(change_idx) != oddv:
        if change_idx not in card_values:
            acceptable[odd_v(change_idx)].add(change_idx)
        change_idx += 1
        if change_idx > m:
            change_idx = 1
        if change_idx == change_idx_start:
            raise CantException()

    res = change_idx
    card_values.add(res)

    change_idx += 1
    if change_idx > m:
        change_idx = 1
    return res


def solve():
    n, m = list(map(int, input().split()))
    cards = list(map(int, input().split()))

    odd_balance = 0
    card_values = set()
    indices_to_be_changed = set()

    for i, c in enumerate(cards):
        odd_balance += odd_v(c)
        if c in card_values:
            indices_to_be_changed.add(i)
        card_values.add(c)

    # print("indices to be changed: ", indices_to_be_changed)
    change_count = len(indices_to_be_changed)

    for i in indices_to_be_changed:
        if odd_v(cards[i]) * odd_balance <= 0:
            #print("Changing ", cards[i])
            cards[i] = change(card_values, odd_v(cards[i]), m)
            #print("Changed to ", cards[i])
        else:
            #print("For teh balance changing ", cards[i])
            odd_balance -= 2 * odd_v(cards[i])
            cards[i] = change(card_values, - odd_v(cards[i]), m)
            #print("Changed to ", cards[i])

    #print("current odd balance:", odd_balance)
    for i in range(len(cards)):
        if odd_balance == 0:
            break
        if odd_v(cards[i]) * odd_balance > 0:
            # print("gonna change")
            change_count += 1
            odd_balance -= 2 * odd_v(cards[i])
            cards[i] = change(card_values, -odd_v(cards[i]), m)

    odd_balance = 0
    for i, c in enumerate(cards):
        odd_balance += odd_v(c)
    if odd_balance != 0:
        print(odd_balance)
        print("WTFFFFF")

    return change_count, cards


def __starting_point():
    try:
        change_cnt, cards = solve()
        print(change_cnt)
        print(" ".join(map(str, cards)))
    except CantException:
        print("-1")

__starting_point()