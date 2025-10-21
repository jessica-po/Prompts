def f(m):
    v = 0
    for x in m:
        v |= x
    return v
input()
print(f(map(int, input().split())) + f(map(int, input().split())))