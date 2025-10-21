#!/usr/bin/env python3

def is_conn(i1, i2):
  a, b = i1
  c, d = i2
  return (c < a < d or c < b < d)

neighbors = {}
intervals = []

n = int(input())
for i in range(0, n):
  q, x, y = [int(j) for j in input().split()]
  if q == 1:
    # we add to the interval
    ourint = (x,y)
    intervals.append(ourint)
    neighbors[ourint] = []
    # and check for edges
    for interval in intervals:
      # if they are connected, join them
      if is_conn(interval, ourint):
        neighbors[interval].append(ourint)
      if is_conn(ourint, interval):
        neighbors[ourint].append(interval)
    
  if q == 2:
    # we check whether there is a path from x to y
    # this is easy version, bfs should be enough
    x -= 1
    y -= 1
    a = intervals[x]
    b = intervals[y]
    
    visited = {a}
    query = [a]
    while len(query) > 0:
        j = query[0]
        query = query[1:]
        for nei in neighbors[j]:
            if not nei in visited:
                query.append(nei)
                visited = visited | {nei}

    if b in visited:
        print("YES")
    else:
        print("NO")