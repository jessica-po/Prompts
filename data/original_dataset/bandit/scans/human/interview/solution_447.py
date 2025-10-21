#!/usr/bin/env python3



def addmod(left, right, modulo=1000000007):
    res = left + right
    if res >= modulo:
        res -= modulo
    return res

def counter(a, m, d):
    res = [0, ] * (2*m)
    res[0] = 1
    shift = 1
    for pos in range(len(a), 0, -1):
        ptype = pos & 1
        cur = int(a[pos-1])
        tres = [0, ] * (2*m)
        for i in range(10):
            if ptype==1 and i == d:
                continue
            if ptype==0 and i != d:
                continue
            k = (i * shift) % m
            for j in range(m):
                k2 = k*2
                j2 = j*2
                if i < cur:
                    tres[k2+0] = addmod(tres[k2+0], addmod(res[j2+0], res[j2+1]))
                elif i == cur:
                    tres[k2+0] = addmod(tres[k2+0], res[j2+0])
                    tres[k2+1] = addmod(tres[k2+1], res[j2+1])
                else:
                    tres[k2+1] = addmod(tres[k2+1], addmod(res[j2+0], res[j2+1]))
                k = k+1 if k+1<m else 0
        res = tres
        shift = (shift * 10) % m
    return res[0]


def solver(ifs):
    m, d = list(map(int, ifs.readline().split()))
    a = ifs.readline().strip()
    b = ifs.readline().strip()
    res = counter(b, m, d)
    if a != '0':
        a = str(int(a) - 1)
        if len(a) < len(b):
            a = '0' + a
        modulo = 1000000007
        res = addmod(res, modulo - counter(a, m, d))
    print(res)

def main():
    import sys
    if sys.version_info.major == 3:
        from io import StringIO as StreamIO
    else:
         from io import BytesIO as StreamIO
    
    with StreamIO(sys.stdin.read()) as ifs, StreamIO() as ofs:
        _stdout = sys.stdout
        sys.stdout = ofs
        solver(ifs)
        sys.stdout = _stdout
        sys.stdout.write(ofs.getvalue())
    return 0

def __starting_point():
    main()

__starting_point()