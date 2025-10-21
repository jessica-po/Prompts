#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
above = n // 3
below = n - above
for i in range(above):
    print(2 * i + 1, 3)
for i in range(below):
    print(i, 0)