n, m, k = list(map(int, input().split()))
print((k - 1) // (2 * m) + 1, end=" ")
print((k - 1) % (2 * m) // 2 + 1, end=" ")
if ((k - 1) % (2 * m) % 2 == 0):
    print("L")
else:
    print("R")