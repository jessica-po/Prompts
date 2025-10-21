#!/usr/bin/env python3

import numpy as np
from scipy.special import comb

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a_sum = np.cumsum(a)


re_list = {}
re_list[0] = 1
for i in a_sum:
    re = i % m
    if re in re_list:
        re_list[re] += 1
    else:
        re_list[re] = 1

# print(re_list)
ans = 0
for value in list(re_list.values()):
    ans += comb(value, 2, exact=True)

print(ans)