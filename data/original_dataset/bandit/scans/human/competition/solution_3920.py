As = list(map(int, input().split()))

def solve(As):
    L = As[0] + As[1] + As[2]
    return L**2 - As[0]**2 - As[2]**2 - As[4]**2

print(max(solve(As), solve(As[1:] + [As[0]])))