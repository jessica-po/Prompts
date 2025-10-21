from bisect import bisect

HISENTINEL = 10**9 + 1
LOSENTINEL = -HISENTINEL

def main():
    length = int(input())
    a = [int(fld) for fld in input().strip().split()]
    b = [int(fld) for fld in input().strip().split()]
    print(countmaxminsubseq(a, b))
    
def countmaxminsubseq(a, b):
    leq, lgt = getleftbounds(a, b, 0)
    req, rgt = getleftbounds(reversed(a), reversed(b), 1)
    req = reverseindex(req)
    rgt = reverseindex(rgt)
    count = 0
    for i, (leq1, lgt1, req1, rgt1) in enumerate(zip(leq, lgt, req, rgt)):
        count += (leq1 - lgt1)*(rgt1 - i) + (i - leq1)*(rgt1 - req1)
    return count
    
def getleftbounds(a, b, bias):
    astack = [(HISENTINEL, -1)]
    bstack = [(LOSENTINEL, -1)]
    leqarr, lgtarr = [], []
    for i, (aelt, belt) in enumerate(zip(a, b)):
        while astack[-1][0] < aelt + bias:
            astack.pop()
        lgt = astack[-1][1]
        while bstack[-1][0] > belt:
            bstack.pop()
        if belt < aelt:
            leq = lgt = i
        elif belt == aelt:
            leq = i
            istack = bisect(bstack, (aelt, -2)) - 1
            lgt = max(lgt, bstack[istack][1])
        else:
            istack = bisect(bstack, (aelt, i)) - 1
            val, pos = bstack[istack]
            if val < aelt:
                lgt = leq = max(lgt, pos)
            else:
                leq = pos
                istack = bisect(bstack, (aelt, -2)) - 1
                val, pos = bstack[istack]
                lgt = max(lgt, pos)
                leq = max(leq, lgt)
                
        leqarr.append(leq)
        lgtarr.append(lgt)
        astack.append((aelt, i))
        bstack.append((belt, i))
    return leqarr, lgtarr
    
def reverseindex(rind):
    pivot = len(rind) - 1
    return [pivot - i for i in reversed(rind)]
    
   
main()