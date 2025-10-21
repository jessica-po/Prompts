for _ in range(int(input())):
    n = int(input())
    x1 = 0
    x2 = 0
    for i in range(1, n//2):
        x1 += 2**i
    for j in range(n//2, n):
        x2 += 2**j
    x1 += 2**n
    print(abs(x1 - x2))