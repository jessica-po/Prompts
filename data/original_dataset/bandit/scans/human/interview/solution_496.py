def isZ(a):
    return a == int(a)
def geom(a,b,c,d):
    if 0 in (a,b,c,d) and not (a==b==c==d==0):
        return False
    if(b/a==c/b==d/c):
        nxt = d * (d/c)
        if not isZ(nxt): return False
        print(int(nxt))
        return True
    return False
def ar(a,b,c,d):
    if(b-a==c-b==d-c):
        print(int(2*d-c))
        return True
    return False

a,b,c,d = map(float,input().split())
if not geom(a,b,c,d) and not ar(a,b,c,d):
    print(42)