a, b, c = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
ans0 = round(abs(x1 - x2) + abs(y1 - y2), 9)
if a * b ==0:
    print(ans0)
    raise SystemExit
x11 = (-c - b * y1) / a
y12 = (-c - a * x1) / b
x21 = (-c - b * y2) / a
y22 = (-c - a * x2) / b

ans1 = abs(x1 - x11) + abs(x21 - x2) + ((y2 - y1)**2 + (x21 - x11)**2)**0.5
ans2 = abs(y1 - y12) + abs(x21 - x2) + ((y2 - y12)**2 + (x21 - x1)**2)**0.5
ans3 = abs(y1 - y12) + abs(y2 - y22) + ((x1 - x2)**2 + (y12 - y22)**2)**0.5
ans4 = abs(x1 - x11) + abs(y22 - y2) + ((x11 - x2)**2 + (y1 - y22)**2)**0.5

ans0 = min(ans0, ans1, ans2, ans3, ans4)

print(round(ans0, 10))