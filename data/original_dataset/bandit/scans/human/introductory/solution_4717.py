x, a, b = (int(x) for x in input().split())
if abs(a-x) < abs(b-x):
    print("A")
else:
    print("B")