#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	sample
# CreatedDate:  2020-10-10 20:29:20 +0900
# LastModified: 2020-10-10 20:37:38 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    A = [0]
    visited = [0]*(N+1)
    for _ in range(N):
        A.append(int(input()))
    i = 1
    cnt = 0
    while visited[i] == 0:
        if i == 2:
            print(cnt)
            return
        cnt += 1
        visited[i] = 1
        i = A[i]
    print((-1))



def __starting_point():
    main()

__starting_point()