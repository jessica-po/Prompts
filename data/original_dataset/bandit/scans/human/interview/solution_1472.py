#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


N, X, Y = MI()
cnt = [0] * N

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        idx = min(j - i, abs(X - i) + abs(Y - j) + 1)
        cnt[idx] += 1

for c in cnt[1:]:
    print(c)