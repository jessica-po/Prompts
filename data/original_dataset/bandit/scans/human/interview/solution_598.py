import bisect
import collections


def solve(inp, *args):
    n, x = list(map(int, inp.split(" ", 1)))
    travels_by_len = collections.defaultdict(list)
    travels_by_len_processed = {}
    for travel in args:
        l, r, cost = list(map(int, travel.split(" ", 2)))
        travels_by_len[r - l + 1].append((l, r, cost))
    for travel_len, travels in list(travels_by_len.items()):
        travels.sort()
        travels_processed = [(travels[-1][0], travels[-1][2])]
        for i in range(len(travels) - 2, -1, -1):
            prev_travel = travels_processed[-1]
            l, r, c = travels[i]
            travels_processed.append((l, min(c, prev_travel[1])))
        travels_by_len_processed[travel_len] = travels_processed[::-1]

    best_price = float("inf")
    for first_travel_len, first_travels in list(travels_by_len.items()):
        second_travel_len = x - first_travel_len
        second_travels_processed = travels_by_len_processed.get(second_travel_len, [])
        for first_travel in first_travels:
            l1, r1, c1 = first_travel
            # now we look for cheapest travels which have l2 > r1
            idx = bisect.bisect_right(second_travels_processed, (r1, float("inf")))
            if 0 <= idx < len(second_travels_processed):
                best_price = min(best_price, c1 + second_travels_processed[idx][1])
    return -1 if best_price == float("inf") else best_price


def __starting_point():
    inp = input()
    n, x = list(map(int, inp.split(" ", 1)))
    print(solve(inp, *(input() for i in range(n))))

__starting_point()