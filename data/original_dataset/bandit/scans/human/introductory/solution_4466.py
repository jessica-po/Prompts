#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x, y, z = list(map(int, input().split()))

print(((x-z)//(y+z)))