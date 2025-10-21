n, h, a, b, k = map(int, input().split())
for i in range(k):
    t1, f1, t2, f2 = map(int, input().split())
    if t1 == t2:
        print(abs(f1 - f2))
    elif f1 >= a and f1 <= b:
        print(abs(t2 - t1) + abs(f2 - f1))
    elif f1 < a:
        print(abs(a - f1) + abs(t2 - t1) + abs(f2 - a))
    elif f1 > b:
        print(abs(b - f1) + abs(t2 - t1) + abs(f2 - b))