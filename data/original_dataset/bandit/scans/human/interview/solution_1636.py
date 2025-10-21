def __starting_point():

    n = int( input() )

    maxX = [-1]*100005
    for _ in range(n):
        px,py = [int(x) for x in input().split()]
        maxX[py] = max( maxX[py] , px )

    #print( maxX[:2] )

    w = [int(x) for x in input().split()]

    p = [-1]*100005
    p[0] = 0
    wdict = dict()
    wdict[0] = (0,0)
    res = []
    for wi in w:
        if wi in wdict:
            px , py = wdict.pop(wi)
            res.append( (px,py) )
            if maxX[py] > px:
                wdict[py-(px+1)] = (px+1,py)
                p[py] += 1
            if maxX[py+1] != -1 and p[py+1] == -1:
                wdict[py+1] = (0,py+1)
                p[py+1] += 1
        else:
            break

    if len(res) == n:
        print("YES")
        for ares in res:
            print(ares[0],ares[1])
    else:
        print("NO")
__starting_point()