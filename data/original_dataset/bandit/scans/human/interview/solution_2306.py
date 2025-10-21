import sys
input = sys.stdin.readline

def main():
    N = int(input())
    t = list(map(lambda x: int(x) * 2, input().split()))
    v = list(map(float, input().split())) + [0]

    for i in range(1, N):
        t[i] += t[i-1]
    t += [t[-1]]
    vnow = [0.0] * (t[-1] + 1)
    vr = [0.0] * (t[-1] + 1)
    r = 0
    for i in range(1, len(vr)):
        if i < t[r]:
            vr[i] = v[r]
        elif i == t[r]:
            vr[i] = min(v[r], v[r+1])
            r += 1
        vnow[i] = min(vnow[i-1] + 0.5, vr[i])
    for i in range(len(vr)-2, -1, -1):
        vnow[i] = min(vnow[i], vnow[i+1] + 0.5)
    
    print(sum(vnow) / 2)

def __starting_point():
    main()
__starting_point()