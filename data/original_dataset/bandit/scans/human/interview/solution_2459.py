# https://codeforces.com/contest/863/problem/D


from sys import stdin, stdout
input = stdin.readline
print = stdout.write
# solve the reversed problem
n, q, m = map(int, input().split())
a = list(map(int, input().split()))
ops = [list(map(int, input().split())) for _ in range(q)]
b = list(map(int, input().split()))


def solve(index, ops):
    def _solve(index, op):
        t, l, r = op
        if index < l or index > r:
            return index
        if t == 1:
            if index == l:
                return r
            else:
                return index - 1
        else:
            return l + r - index

    for op in ops[::-1]:
        index = _solve(index, op)
    return index


b = list(map(lambda x: solve(x, ops), b))
for i in b:
    print(str(a[i-1])+" ")

# Cartesian tree:
# https://codeforces.com/contest/863/submission/30693678