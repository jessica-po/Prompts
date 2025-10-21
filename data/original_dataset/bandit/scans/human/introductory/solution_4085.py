for q in range(int(input())):
    n = int(input())
    D = list(map(int, input().split()))
    D.sort()
    z = D[0] * D[-1]
    if z == -1:
        print(-1)
    else:
        Dz = set()
        for i in range(2, int(z ** 0.5) + 1):
            if z % i == 0:
                Dz.add(i)
                Dz.add(z // i)
        if Dz == set(D):
            print(z)
        else:
            print(-1)