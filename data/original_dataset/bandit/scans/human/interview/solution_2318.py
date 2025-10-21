#!/usr/bin/env python
import sys
input = sys.stdin.readline


def cnt(s):
    l = [[s[0], 1]]
    for c in s[1:]:
        if l[-1][0] == c:
            l[-1][1] += 1
        else:
            l.append([c, 1])
    return l


def cmp(sc, tc):
    if len(tc) != len(sc):
        # print(f'sc = {sc}, tc = {tc}')
        return False
    for i in range(len(tc)):
        if tc[i][0] != sc[i][0] or tc[i][1] < sc[i][1]:
            # print(f'sc = {sc}, tc = {tc}, i = {i}')
            return False
    return True


for _ in range(int(input())):
    s, t = input().strip(), input().strip()
    sc, tc = cnt(s), cnt(t)
    print('YES' if cmp(sc, tc) else 'NO')