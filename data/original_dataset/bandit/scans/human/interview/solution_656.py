#!/usr/bin/env python3
def solve():
    n, k = list(map(int, input().split()))
    temps = list(map(int, input().split()))

    summer_seqs = []
    winter_seqs = []

    cur_season = 1
    cur_len = 0
    for t in temps:
        # print("Handling", t)
        if cur_season * t > 0 or (t == 0 and cur_season == 1):
            cur_len += 1
            # print("Adding...")
        else:
            # print("Thats new!")
            if cur_season == 1:
                summer_seqs.append(cur_len)
            else:
                winter_seqs.append(cur_len)
            cur_len = 1
            cur_season = -cur_season
    if cur_season == 1:
        summer_seqs.append(cur_len)
    else:
        winter_seqs.append(cur_len)

    summer_seqs = summer_seqs[1:]

    cur_len = sum(winter_seqs)

    if cur_len > k:
        return -1

    if len(summer_seqs) == 0:
        return 1 if len(winter_seqs) != 0 else 0

    changes = len(summer_seqs) + len(winter_seqs)

    last_sum_seq = None
    if temps[-1] >= 0:
        last_sum_seq = summer_seqs[-1]
        summer_seqs = summer_seqs[:-1]

    summer_seqs = list(sorted(summer_seqs))

    # print("Changes needed so far:", changes)
    # print("Summer seqs: ", len(summer_seqs))
    # print("Last summer seq:", last_sum_seq)
    # print("Can drive for another", k - cur_len)

    for s in summer_seqs:
        if k - cur_len >= s:
            changes -= 2
            cur_len += s
        else:
            break

    # print("Before last summer we can drive for",
    #       k - cur_len, "having ", changes, "changes")

    if last_sum_seq is not None:
        if k - cur_len >= last_sum_seq:
            # print("and dont change at last")
            changes -= 1

    return changes


def __starting_point():
    print(solve())

__starting_point()