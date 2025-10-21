def main():
    N = int(input())
    A = list(map(int, input().split()))
    alice = 0
    bob = 0
    A.sort(reverse=True)
    for i, a in enumerate(A):
        if i%2 == 0:
            alice += a
        else:
            bob += a
    print((alice - bob))

def __starting_point():
    main()

__starting_point()