t, sx, sy, ex, ey = map(int, input().split())
d = {'W':max(0, sx - ex), 'E':max(0, ex - sx), 'N':max(0, ey - sy), 'S':max(0, sy - ey)}
for (i, c) in enumerate(input(), 1):
  if d[c] > 0:
    d[c] -= 1
  if any(d.values()) == False:
    print(i)
    break
else:
  print(-1)