def doit():
    xx = input().split()
    n = int(xx[0])
    s = int(xx[1])
    v = [int(k) for k in input().split()]

    S = sum(v)
    newS = S - s
    if newS < 0:
        return -1
    return min(newS//n, min(v))
        
print(doit())