def main():
    n, m = map(int, input().split())
    def intCompare(x):
        if int(x) == m:
            return 0
        if int(x) < m:
            return -1
        return 1
    p = list(map(intCompare, input().split()))
    ret = 0
    ind = p.index(0)
    tem = 0
    ret0 = [0] * 400001
    ret1 = [0] * 400001
    set0 = set()
    for i in range(ind, -1, -1):
        tem += p[i]
        ret0[tem] += 1
        set0.add(tem)
    tem = 0
    for i in range(ind, n):
        tem += p[i]
        ret1[tem] += 1
    for i in set0:
        ret += ret0[i] * (ret1[-i] + ret1[1-i]) 
    print(ret)
    return 0
main()