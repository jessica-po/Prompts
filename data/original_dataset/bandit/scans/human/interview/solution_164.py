y1, y2, w, x, y, r = map(int, input().strip().split())
w -= r
y1 = 2 * w - y1 - y - r
y2 = 2 * w - y2 - y
if x * x * (y2 - y1) * (y2 - y1) <= (y1 * y1 + x * x) * r * r:
  print(-1)
else:
  print(f"{x * (y1 + y - w) / y1:.10f}")