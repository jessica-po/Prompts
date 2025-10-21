#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

b_a = {}
for n_ in range(n):
    b, a = input().split()

    replaced = False
    for k in b_a:
        if b_a[k] == b:
            b_a[k] = a
            replaced = True
    if not replaced:
        b_a[b] = a

print(len(b_a))
for k in b_a:
    print(k + " " + b_a[k])