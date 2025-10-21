n = int(input())
a = [int(ai) for ai in input().split()]

def solve(x):
    n = len(x)
    if sorted(x) == x:
        return n
    return max(solve(x[:n//2]), solve(x[n//2:]))

print(solve(a))