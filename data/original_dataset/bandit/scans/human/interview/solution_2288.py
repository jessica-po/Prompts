t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    if list(sorted(a)) == a or not all(x == b[0] for x in b):
        print("Yes")
    else:
        print("No")