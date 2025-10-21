class RedBlackNode(object):

    def __init__(self, key):
        self._key = key
        self._red = False
        self._left = None
        self._right = None
        self._p = None


class RedBlackTree(object):

    def __init__(self):
        self._nil = RedBlackNode(None)
        self._root = self._nil

    def insert_key(self, key):
        y = self.search(key, True)
        z = RedBlackNode(key)
        z._p = y
        if y == self._nil:
            self._root = z
        elif z._key < y._key:
            y._left = z
        else:
            y._right = z
        z._left = self._nil
        z._right = self._nil
        z._red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z._p._red:
            if z._p == z._p._p._left:
                y = z._p._p._right
                if y._red:
                    z._p._red = False
                    y._red = False
                    z._p._p._red = True
                    z = z._p._p
                else:
                    if z == z._p._right:
                        z = z._p
                        self._left_rotate(z)
                    z._p._red = False
                    z._p._p._red = True
                    self._right_rotate(z._p._p)
            else:
                y = z._p._p._left
                if y._red:
                    z._p._red = False
                    y._red = False
                    z._p._p._red = True
                    z = z._p._p
                else:
                    if z == z._p._left:
                        z = z._p
                        self._right_rotate(z)
                    z._p._red = False
                    z._p._p._red = True
                    self._left_rotate(z._p._p)
        self._root._red = False

    def _left_rotate(self, x):
        y = x._right
        x._right = y._left
        if y._left != self._nil:
            y._left._p = x
        y._p = x._p
        if x._p == self._nil:
            self._root = y
        elif x == x._p._left:
            x._p._left = y
        else:
            x._p._right = y
        y._left = x
        x._p = y

    def _right_rotate(self, y):
        x = y._left
        y._left = x._right
        if x._right != self._nil:
            x._right._p = y
        x._p = y._p
        if y._p == self._nil:
            self._root = x
        elif y == y._p._right:
            y._p._right = x
        else:
            y._p._left = x
        x._right = y
        y._p = x

    def search(self, key, s):
        x = self._root
        g = self._nil
        while x != self._nil:
            g = x
            if key < x._key:
                x = x._left
            else:
                x = x._right
        return(g)
    def search2(self, key):
        a = None
        b = None
        x = self._root
        while x != self._nil and key != x._key:
            if key < x._key:
                a = x
                x = x._left
            else:
                b = x
                x = x._right
        if key == x._key:
            return(None)
        else:
            return((a,b))


n = int(input())
s = [int(i) for i in input().split()]
t = RedBlackTree()
t.insert_key([s[0],0,0])
    
e = []
for i in s[1:]:
    o,u = t.search2([i,0,0])
    if u == None:
        e.append(o._key[0])
        if o._key[0] > i:
            o._key[1] = 1
        else:
            o._key[2] = 1
    elif o == None:
        e.append(u._key[0])
        if u._key[0] > i:
            u._key[1] = 1
        else:
            u._key[2] = 1
    else:
        if o._key[0] > i and u._key[0] > i:
            if o._key[1] == 0:
                o._key[1] = 1
                e.append(o._key[0])
            else:
                u._key[1] = 1
                e.append(u._key[0])
            
        elif o._key[0] < i and u._key[0] > i:
            if o._key[2] == 0:
                o._key[2] = 1
                e.append(o._key[0])
            else:
                u._key[1] = 1
                e.append(u._key[0])
        elif o._key[0] > i and u._key[0] < i:
            if o._key[1] == 0:
                o._key[1] = 1
                e.append(o._key[0])
            else:
                u._key[2] = 1
                e.append(u._key[0])
        elif o._key[0] < i and u._key[0] < i:
            if o._key[2] == 0:
                o._key[2] = 1
                e.append(o._key[0])
            else:
                u._key[2] = 1
                e.append(u._key[0])
    t.insert_key([i,0,0])
print(*e)