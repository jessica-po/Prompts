def prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for d in range(3, x, 2):
        if d * d > x:
            break
        if x % d == 0:
            return False

    return True

def main():
    n = int(input())
    for m in range(1, 1001):
        if not prime(n * m + 1):
            ans = m
            break

    print(ans)

main()