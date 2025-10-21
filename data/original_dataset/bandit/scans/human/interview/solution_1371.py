#!/usr/bin/env python

def main():
    s = int(input())
    mod = 10**9 + 7
    a_lst = [1, 0, 0]
    a_sum = 0

    if s >= 3:
        for i in range(3, s+1):
            a_sum += a_lst[i-3]
            a_sum %= mod
            a_lst.append(a_sum)

    print((a_lst[s]))

def __starting_point():
    main()

__starting_point()