from itertools import accumulate
import sys

def solve(f, g):
    n, m, k, s = [int(x) for x in f.readline().split()]
    a_price = [(int(x), i+1) for i, x in enumerate(f.readline().split())]
    b_price = [(int(x), i+1) for i, x in enumerate(f.readline().split())]

    a_gadgets = []
    b_gadgets = []
    for i, line in enumerate(f):
        t, price = [int(x) for x in line.split()]
        if t == 1:
            a_gadgets.append((price, i + 1))
        else:
            b_gadgets.append((price, i + 1))

    a_gadgets.sort()
    b_gadgets.sort()

    prefix_a = [0] + list(accumulate(gadget[0] for gadget in a_gadgets))
    prefix_b = [0] + list(accumulate(gadget[0] for gadget in b_gadgets))

    la = min(k, len(a_gadgets))
    lb = min(k, len(b_gadgets))
    min_price_for_k = [(prefix_a[i], prefix_b[k - i], i) for i in range(k-lb, la+1)]

    for i in range(1, n):
        a_price[i] = min(a_price[i], a_price[i-1])
        b_price[i] = min(b_price[i], b_price[i-1])
        
    def expence(day):
        return lambda x: a_price[day][0]*x[0] + b_price[day][0]*x[1]

    x, y = 0, n-1
    while x <= y-1:
        day = (x + y) // 2
        min_cost = min(min_price_for_k, key = expence(day))
        if expence(day)(min_cost) > s:
            x = day+1
        else:
            y = day
    min_cost = min(min_price_for_k, key = expence(x))
    if expence(x)(min_cost) > s:
        g.write('-1\n')
    else:
        g.write(str(x+1) + '\n')
        i1 = min_cost[-1]
        A, B = ' ' + str(a_price[x][1]) + '\n', ' ' + str(b_price[x][1]) + '\n'
        for i in range(i1):
            g.write(str(a_gadgets[i][1]) + A)
        for i in range(k - i1):
            g.write(str(b_gadgets[i][1]) + B)

solve(sys.stdin, sys.stdout)