import sys
f = sys.stdin
#f = open("input.txt", "r")
a = [list(map(int, i.split())) for i in f.read().strip().split("\n")]
def solve():
    s = a[0][2] + a[2][0]
    for i in range(1, s):
        a[0][0] = i
        a[2][2] = s-i
        if sum(a[0]) == sum(a[2]):
            break
    a[1][1] = sum(a[0]) - sum(a[1])
    for i in a:
        print(*i)
solve()