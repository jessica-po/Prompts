#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Code by H~$~C

from sys import stdin
input = stdin.readline
import math

n = int(input())
G = [[] for i in range(n + 1)]
for i in range(n - 1):
  u, v = map(int, input().split())
  G[u].append([v, i])
  G[v].append([u, i])

ans = [-1] * (n + 1)

for u in range(1, n + 1):
  if (len(G[u]) >= 3):
    for j in range(len(G[u])):
      ans[G[u][j][1]] = j
    cnt = len(G[u])
    for j in range(n - 1):
      if (ans[j] == -1):
        ans[j] = cnt
        cnt += 1
    for j in range(n - 1):
      print(ans[j])
    return

for i in range(n - 1):
  print(i)