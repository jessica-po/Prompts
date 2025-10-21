#return if sa contains a real prefix: sb
def isPrefix( sa , sb ):
    if len(sa) <= len(sb):
        return False
    return sa[0:len(sb)] == sb

def getOrder( sa , sb ):
    for i in range( 0 , min( len(sa) , len(sb) ) ):
        if sa[i] != sb[i]:
            return sa[i],sb[i]

test = False
if test:
    fp = open("C-4.in","r")
    n = int(fp.readline().strip())
    names = [ fp.readline().strip() for i in range(0,n)]
    fp.close()
else:
    n = int(input().strip())
    names = [ input().strip() for i in range(0,n)]

g = [[False]*26 for i in range(0,26)]

res = True
for i in range(1,n):
    if names[i-1] == names[i] or isPrefix( names[i] , names[i-1] ):
        continue
    elif isPrefix( names[i-1] , names[i] ):
        res = False
        break
    else:
        ca,cb = getOrder( names[i-1] , names[i] )
        #print(ca,"<",cb)
        if g[ord(cb)-ord('a')][ord(ca)-ord('a')]:
            res = False
            break
        else:
            g[ord(ca)-ord('a')][ord(cb)-ord('a')] = True

def printG():
    print("  abcdefghijklmnopqrstuvwxyz")
    for i in range(0,26):
        print( chr( ord("a") + i ) , "".join( [ "1" if x else "0" for x in g[i]] ) , sep = "")
#printG()

if not res:
    print("Impossible")
else:

    def getZeroIndegreeNode():
        for i in range(0,26):
            if not used[i] and indegree[i] == 0:
                return i
        return -1
    #topo sort
    theOrder = []
    indegree = [0] * 26
    used = [False] * 26

    #calc indegree
    for i in range(0,26):
        ithIndegree = 0
        for j in range(0,26):
            if g[j][i]: ithIndegree += 1
        indegree[i] = ithIndegree
        
    for i in range(0,26):
        zeroIndegreeNode = getZeroIndegreeNode()
        if zeroIndegreeNode == -1:
            res = False
            break
        else:
            used[zeroIndegreeNode] = True
            theOrder.append( chr( ord('a') + zeroIndegreeNode ) )
            for j in range(0,26):
                if g[zeroIndegreeNode][j]:
                    indegree[j] -= 1

    if not res:
        print("Impossible")
    else:
        print( "".join( theOrder ) )