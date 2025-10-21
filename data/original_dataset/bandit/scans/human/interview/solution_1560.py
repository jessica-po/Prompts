#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(first, s):
    second = 'r' if first == 'b' else 'b'
    alt = [first, second]

    error = [0, 0]
    for i,ch in enumerate(s):
        shouldbe = alt[i % 2]
        if ch != shouldbe:
            error[i % 2] += 1

    return max(error)

def main():
    n = int(input())
    s = input()
    print(min(f('r', s), f('b', s)))

main()