#!/usr/bin/env python3


def main():
    n = int(input())
    ps = [int(x) for x in input().split()]
    v = set('aeiouy')
    for p in ps:
        s = input()
        ss = sum(1 for x in s if x in v)
        if ss != p:
            print('NO')
            return
    print('YES')


def __starting_point():
    main()

__starting_point()