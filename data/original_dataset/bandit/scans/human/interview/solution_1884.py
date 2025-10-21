# python3

def readline(): return tuple(map(int, input().split()))


def ceil_div(num, den): return (num - 1) // den + 1


def main():
    n, x1, x2 = readline()
    c = readline()

    xx = (x1, x2)

    servers = sorted(enumerate(c, start=1), key=lambda p: p[1])
    for (i, a) in enumerate(servers):
        for (j, x) in enumerate(xx):
            kj = ceil_div(x, a[1])
            if i + kj < n and (n - i - kj) * servers[i + kj][1] >= sum(xx) - x:
                print("Yes")
                l1 = servers[i:i+kj]
                l2 = servers[i+kj:]
                if j: l1, l2 = l2, l1
                print(len(l1), len(l2))
                print(" ".join(str(d[0]) for d in l1))
                print(" ".join(str(d[0]) for d in l2))
                return
    print("No")


main()




# Made By Mostafa_Khaled