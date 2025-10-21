#!/usr/bin/env python3
from itertools import accumulate
from heapq import heappop, heappush


def top(ppl_indices, vals, start):
    Q = []
    res = [0 for i in range(len(ppl_indices))]
    for k, idx in enumerate(ppl_indices):
        heappush(Q, -vals[idx])
        if k >= start:
            res[k] = res[k-1] - heappop(Q)

    return res


n, a_size, b_size = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

conversion_gain = [y - x for x, y in zip(a, b)]

ordered_by_a = sorted(zip(a, list(range(n))), reverse=True)
prefix_sums_a = list(accumulate([x for x, y in ordered_by_a]))
conversions = top([idx for val, idx in ordered_by_a], conversion_gain, a_size)
rest_of_bs = list(reversed(top([idx for val, idx in reversed(ordered_by_a[a_size:])],
                               b, n - a_size - b_size))) + [0]

sol, top_k = max([(prefix_a + convert + add_bs, idx)
                  for idx, (prefix_a, convert, add_bs)
                  in enumerate(zip(prefix_sums_a[a_size-1:a_size+b_size],
                                   conversions[a_size-1:a_size+b_size],
                                   rest_of_bs))])
top_k += a_size

conversion_ordered_by_a = [(conversion_gain[idx], idx) for val, idx in ordered_by_a]
conversion_sorted = sorted(conversion_ordered_by_a[:top_k], reverse=True)
converted = [idx for val, idx in conversion_sorted[:top_k-a_size]]
team_a = list(set(idx for val, idx in ordered_by_a[:top_k]) - set(converted))

b_ordered_by_a = [(b[idx], idx) for val, idx in ordered_by_a]
b_sorted = sorted(b_ordered_by_a[top_k:], reverse=True)
team_b = converted + [idx for val, idx in b_sorted[:(a_size+b_size) - top_k]]

print(sol)
print(" ".join(str(idx+1) for idx in team_a))
print(" ".join(str(idx+1) for idx in team_b))