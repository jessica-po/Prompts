n, m = list(map(int, input().split()))
for i in range(n):
    for j in input().split():
        if j in "CMY":
            print("#Color")
            return
print("#Black&White")