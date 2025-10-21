ans = {}

def gen(n, k, d, used = False):
    if not ans.get((n, k, d, used)):
        if not n and used:
            ans[(n, k, d, used)] = 1
        else:
            ans[(n, k, d, used)] = sum(gen(n - x, k, d, used or x >= d) for x in range(1, min(n, k) + 1) if max(x, n - x) >= d or used)
    return ans[(n, k, d, used)]


n, k, d = list(map(int, input().split()))
print(gen(n, k, d)  % 1000000007)