#!/usr/bin/env python3
import sys
from itertools import chain
import numpy as np


def solve(X: int):
    if X <= 2:
        return 2
    flags = np.array([True for i in range(3, X + 112, 2)])
    for i in range(len(flags)):
        if flags[i]:
            prime = i * 2 + 3
            flags[i::prime] = False
            if prime >= X:
                return prime




def main():
    X = int(input())  # type: int
    answer = solve(X)
    print(answer)


def __starting_point():
    main()

__starting_point()