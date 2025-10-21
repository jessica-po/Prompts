g = "ACTG"

def dist(a, b):
    p = abs(ord(a) - ord(b))
    return min(p, 26 - p)

def price(s):
    return sum(dist(x, y) for x, y in zip(g, s))

n = int(input())
s = input()
ans = 100000
for i in range(len(s) - 3):
    ans = min(ans, price(s[i:i+4]))
print(ans)