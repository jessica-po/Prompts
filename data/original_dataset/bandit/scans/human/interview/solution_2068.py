import sys

def main():
    mx = 1
    n = int(input())
    D = {}
    D["polycarp"] = 1
    for i in range(n):
        s, r, t = input().split()
        s = s.lower()
        t = t.lower()
        D[s] = D[t] + 1
        mx = max(mx, D[s])
    print(mx)

main()