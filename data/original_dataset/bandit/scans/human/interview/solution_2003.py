# 10
# + 8
# + 9
# + 11
# + 6
# + 1
# ? 3
# - 8
# ? 3
# ? 8
# ? 11

MAX_BIT = 30

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.leftCnt = 0
        self.rightCnt = 0
    
    def AddRight(self):
        if self.right == None:
            self.right = Node()
            self.rightCnt = 1
        else:
            self.rightCnt += 1
    
    def AddLeft(self):
        if self.left == None:
            self.left = Node()
            self.leftCnt = 1
        else:
            self.leftCnt += 1

    def RemRight(self):
        self.rightCnt -= 1
    
    def RemLeft(self):
        self.leftCnt -= 1

    def Left(self):
        return self.left != None and self.leftCnt > 0

    def Right(self):
        return self.right != None and self.rightCnt > 0

def insert(u, num, dig=MAX_BIT):
    if dig < 0:
        return
    
    bit = (num>>dig)&1
    if bit > 0: #insert to right
        u.AddRight()
        insert(u.right, num, dig-1)
    else:
        u.AddLeft()
        insert(u.left, num, dig-1)

def remove(u, num, dig=MAX_BIT):
    if dig < 0:
        return
    
    bit = (num>>dig)&1
    if bit > 0: #remove right
        u.RemRight()
        remove(u.right, num, dig-1)
    else:
        u.RemLeft()
        remove(u.left, num, dig-1)

def cal(u, num, dig=MAX_BIT):
    if dig < 0 or u == None:
        return 0
    
    bit = (num>>dig)&1
    if bit > 0: #try to go to left first
        if u.Left(): #if valid
            return (1<<dig) + cal(u.left, num, dig-1)
        elif u.Right():
            return cal(u.right, num, dig-1)
    else: #try to go to right first
        if u.Right():
            return (1<<dig) + cal(u.right, num, dig-1)
        elif u.Left():
            return cal(u.left, num, dig-1)
    return 0

def main():
    root = Node()
    insert(root, 0)

    n = int(input())
    for i in range(n):
        tmp = input().split()
        num = int(tmp[1])
        if tmp[0] == "+":
            insert(root, num)
        elif tmp[0] == "-":
            remove(root, num)
        else:
            print(cal(root, num))

main()