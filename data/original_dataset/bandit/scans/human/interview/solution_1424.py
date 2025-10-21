def check(i):
    x, counter = armies[i] ^ armies[-1], 0
    while x:
        counter += x & 1
        x >>= 1
    return counter <= k

n, m, k = list(map(int, input().split()))
armies = [int(input()) for x in range(m + 1)]
print(sum(map(check, list(range(m)))))