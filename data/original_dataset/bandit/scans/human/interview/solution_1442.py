#!/usr/bin/env python3
import collections

n, s = list(map(int, input().split()))

buy_orders = collections.defaultdict(int)
sell_orders = collections.defaultdict(int)

for i in range(n):
    d, p, q = input().split()
    p, q = int(p), int(q)

    if d == 'B':
        buy_orders[p] += q
    else:
        sell_orders[p] += q

buy_orders = sorted(list(buy_orders.items()), reverse=True)
sell_orders = sorted(list(sell_orders.items()), reverse=True)

for order in sell_orders[-s:]:
    print('S', order[0], order[1])
for order in buy_orders[:s]:
    print('B', order[0], order[1])