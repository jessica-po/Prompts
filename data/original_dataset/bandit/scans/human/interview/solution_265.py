#  author: ThePonyCoder
#  created: 23.06.2019, 21:58
#  filename: f.py
#  path: C:/Users/User/Desktop/python/Prog/CodeForces/rounds/cf_568/f.py

import os

# import random

# sys.setrecursionlimit(999999999)
import string

from math import inf
from functools import lru_cache

if os.getcwd() == 'C:\\Users\\User\\Desktop\\python\\Prog\\CodeForces' \
        or os.environ['COMPUTERNAME'] == 'USER145':
    import pdb
    
    import sys
    
    pdb = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout)
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    from pprint import pprint
    from hypothesis import given, settings
    from hypothesis import strategies as st


def ri():
    return [int(i) for i in input().split()]


def to_bits(l):
    ans = 0
    for i in l:
        ans |= (1 << i - 1)
    return ans


user_masks = [0 for i in range(1 << 10)]
pizzas = [[] for i in range(1 << 10)]


@lru_cache()
def count_sat_users(mask):
    ans = 0
    cmask = mask
    while cmask:
        ans += user_masks[cmask]
        cmask = (cmask - 1) & mask
    return ans


def main():
    n, m = ri()
    for _ in range(n):
        k, *a = ri()
        bits = to_bits(a)
        user_masks[bits] += 1
    
    ans = (float(-inf), float(inf), -1, -1)
    
    for i in range(m):
        c, k, *a = ri()
        bits = to_bits(a)
        pizzas[bits].append((c, i + 1, bits))  # цена, номер, маска
        pizzas[bits].sort()
        while len(pizzas[bits]) > 2:
            pizzas[bits].pop()
    # pprint(pizzas)
    
    for mask_F in range(1 << 9):
        for mask_S in range(1 << 9):
            if len(pizzas[mask_F]) and len(pizzas[mask_S]) \
                    and mask_F != mask_S:
                
                mask = mask_F | mask_S
                
                satisfied_users = count_sat_users(mask)
                
                f_pizza = next(iter(pizzas[mask_F]))
                s_pizza = next(iter(pizzas[mask_S]))
                
                summary_cost = 0
                summary_cost += f_pizza[0]
                summary_cost += s_pizza[0]
                
                ans = max(ans,
                          (satisfied_users,
                           -summary_cost,
                           s_pizza[1],
                           f_pizza[1]))
                
                # bruting all masks
                bmask = mask
                while bmask:
                    satisfied_users += user_masks[bmask]
                    bmask = (bmask - 1) & mask
            
            if len(pizzas[mask_F]) == 2:
                satisfied_users = count_sat_users(mask_F)
                
                it = iter(pizzas[mask_F])
                
                f_pizza = next(it)
                s_pizza = next(it)
                summary_cost = 0
                summary_cost += f_pizza[0] + s_pizza[0]
                ans = max(ans,
                          (satisfied_users,
                           -summary_cost,
                           s_pizza[1],
                           f_pizza[1]))
            
            if len(pizzas[mask_S]) == 2:
                satisfied_users = count_sat_users(mask_S)
                
                it = iter(pizzas[mask_S])
                
                f_pizza = next(it)
                s_pizza = next(it)
                summary_cost = 0
                summary_cost += f_pizza[0] + s_pizza[0]
                ans = max(ans,
                          (satisfied_users,
                           -summary_cost,
                           s_pizza[1],
                           f_pizza[1]))
    
    aans = [ans[2],ans[3]]
    aans.sort()
    print(*aans, sep=' ')


main()