def sign(x):
    return (x > 0) - (x < 0)


def key(ab):
    a, b = ab
    return (2, -a - b) if b < 0 else (1, a)


def main():
    n, r = list(map(int, input().split()))
    for a, b in sorted((tuple(map(int, input().split())) for _ in range(n)), key=key):
        if r < a:
            r = -1
            break
        r += b
    if r < 0:
        print("NO")
    else:
        print("YES")


main()