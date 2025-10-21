import math
A,B,X = map(int,input().split())
def Price(N):
    d = math.floor(math.log10(N))+1
    return A*N+B*d
if Price(1) > X:
    Answer = 0
else:
    lef = 1
    rig = 10**9
    for i in range(100):
        mid = (lef+rig)//2
        if Price(mid) <= X:
            Answer = mid
            lef = mid
        else:
            rig = mid
    if Price(rig) <= X:
        Answer = rig
print(Answer)