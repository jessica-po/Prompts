M = 10 ** 9 + 7
def solve1(x):
    n = len(x)
    x = int(x, 2)
    ans = 0
    for a in range(2 ** n):
        for c in range(2 ** n):
            b = a ^ x
            d = c ^ x
            if a < c and b > d:
                ans += 1
    return ans % M

def solve2(x):
    return int(x, 2) * pow(2, (len(x) - 1), M) % M

x = input()
# print(solve1(x))
print(solve2(x))