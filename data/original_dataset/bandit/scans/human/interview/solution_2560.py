t = int(input())
for i in range(0, t) :
    n, l, r = [int(s) for s in input().split()]
    print('Yes' if n % l <= (r - l) *  (n // l) else 'No')