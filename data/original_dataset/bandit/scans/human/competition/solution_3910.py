import sys

def solve():
    n = int(input())
    partner = [0]*(2*n)
    pacani = []
    for line in sys.stdin:
        pacan, telka = [int(x) - 1 for x in line.split()]
        partner[pacan] = telka
        partner[telka] = pacan
        pacani.append(pacan)

    khavka = [None]*(2*n)
    for i in range(2*n):
        while khavka[i] is None:
            khavka[i] = 1
            khavka[i^1] = 2
            i = partner[i^1]

    for pacan in pacani:
        print(khavka[pacan], khavka[partner[pacan]])
    
solve()