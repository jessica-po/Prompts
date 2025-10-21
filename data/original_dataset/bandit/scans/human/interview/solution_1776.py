from math import inf

class Node:
    def __init__(self, parent = None, leftExp = None, rightExp = None, signQ = 0):
        self.parent, self.leftExp, self.rightExp, self.signQ = parent, leftExp, rightExp, signQ
    def __str__(self):
        return "Node"

memo = {}

def Memoize(node, p, maxValue, minValue):
    if not node in memo:
        memo.update({node : {p : [maxValue, minValue]} })
    else:
        memo[node].update({p : [maxValue, minValue]})

def ExpMaxValue(root: Node, p):

    m = root.signQ - p
    """if root.signQ == 1:
        if p == 1:
            return [root.leftExp.value + root.rightExp.value, root.leftExp.value + root.rightExp.value]
        else:
            return [root.leftExp.value - root.rightExp.value, root.leftExp.value - root.rightExp.value]"""

    if root.signQ == 0:
        return [root.value, root.value]
    
    if root in memo:
        if p in memo[root]:
            return memo[root][p]

    if m == 0:
        value = ExpMaxValue(root.leftExp, root.leftExp.signQ)[0] + ExpMaxValue(root.rightExp, root.rightExp.signQ)[0]
        Memoize(root, p, value, value)
        return [value, value]
    if p == 0:
        value = ExpMaxValue(root.leftExp, 0)[0] - ExpMaxValue(root.rightExp, 0)[0]
        Memoize(root, p, value, value)
        return [value, value]
        
    maxValue = -inf
    minValue = inf
    if m >= p:
        for pQMid in range(2):
            pQLeftMin = min(p - pQMid, root.leftExp.signQ)
            for pQLeft in range(pQLeftMin + 1):
                if root.leftExp.signQ - pQLeft + (1 - pQMid) > m:
                    continue
                
                resLeft = ExpMaxValue(root.leftExp, pQLeft)
                resRight = ExpMaxValue(root.rightExp, p - pQMid - pQLeft)
                
                if pQMid == 1:
                    maxValue = max(resLeft[0] + resRight[0], maxValue)
                    minValue = min(resLeft[1] + resRight[1], minValue)
                else:
                    maxValue = max(resLeft[0] - resRight[1], maxValue)
                    minValue = min(resLeft[1] - resRight[0], minValue)
    else:
        for mQMid in range(2):
            mQLeftMin = min(m - mQMid, root.leftExp.signQ)
            for mQLeft in range(mQLeftMin + 1):
                pQLeft = root.leftExp.signQ - mQLeft
                if pQLeft + (1 - mQMid) > p:
                    continue
                
                resLeft = ExpMaxValue(root.leftExp, pQLeft)
                resRight = ExpMaxValue(root.rightExp, p - (1 - mQMid) - pQLeft)
                
                if mQMid == 0:
                    maxValue = max(resLeft[0] + resRight[0], maxValue)
                    minValue = min(resLeft[1] + resRight[1], minValue)
                else:
                    maxValue = max(resLeft[0] - resRight[1], maxValue)
                    minValue = min(resLeft[1] - resRight[0], minValue)

    Memoize(root, p, int(maxValue), int(minValue))

    return [int(maxValue), int(minValue)]
                
                

def PrintNodes(root: Node):
    if root.signQ != 0:
        leftExp = root.leftExp if root.leftExp.signQ != 0 else root.leftExp.value
        rightExp = root.rightExp if root.rightExp.signQ != 0 else root.rightExp.value
        check = root.signQ == root.leftExp.signQ + root.rightExp.signQ + 1
        print(root.signQ, root.parent, leftExp, rightExp, check)
        PrintNodes(root.leftExp)
        PrintNodes(root.rightExp)

        

def main():
    exp = str(input())
    if len(exp) == 1:
        print(exp)
        return
    
    #root = Node(None, None, None)
    #root.parent = root
    cNode = Node()
    isRight = False
    
    for i in range(1, len(exp) - 1):
        if exp[i] == '(':
            if not isRight:
                cNode.leftExp = Node(cNode)
                cNode = cNode.leftExp
            else:
                cNode.rightExp = Node(cNode)
                cNode = cNode.rightExp
            isRight = False
        elif exp[i] == '?':
            isRight = True
            cNode.signQ += 1
        elif exp[i] == ')':
            if cNode.parent != None:
                cNode.parent.signQ += cNode.signQ
            cNode = cNode.parent
            isRight = False
        else:
            if not isRight:
                cNode.leftExp = Node(cNode)
                cNode.leftExp.value = int(exp[i])
            else:
                cNode.rightExp = Node(cNode)
                cNode.rightExp.value = int(exp[i])

    
    #PrintNodes(cNode)

    ss = str(input()).split()
    p, m = int(ss[0]), int(ss[1])

    print(ExpMaxValue(cNode, p)[0])
    


    

main()