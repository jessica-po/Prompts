w, h = map(int, input().split())
u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())

for i in range(h, -1, -1):
    w += i
    if i == d1:
        w = max(w - u1, 0)
    elif i == d2:
        w = max(w - u2, 0)

print(w)