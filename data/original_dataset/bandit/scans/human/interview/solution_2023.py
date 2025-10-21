import sys
'''
SEGMENT TREE
Assign
'''
class SegmTree():
    '''
    - modify elements on interval
    - get single element
    '''
    def __init__(self, size):
        N = 1
        while N < size:
            N <<= 1
        self.N = N
        self.tree = [0] * (2*N)

    def modify_range(self, l, r, value):
        l += self.N
        r += self.N
        while l < r:
            if l & 1:
                self.tree[l] = value
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] = value
            l >>= 1
            r >>= 1
    
    def query(self, i):
        i += self.N
        latest_change = self.tree[i]
        p = i
        while p > 1:
            p >>= 1
            latest_change = max(latest_change, self.tree[p])
        return latest_change

# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, line.split())) for line in sys.stdin)
input = reader.__next__

n, m = input()
a = list(input())
b = list(input())
st = SegmTree(n)
request = [None] * (m + 1)
for i in range(1, m+1):
    t, *arg = input()
    if t == 1:
        x, y, k = request[i] = arg
        st.modify_range(y-1, y-1+k, i)
    else:
        pos = arg[0] - 1
        req_id = st.query(pos)
        if req_id > 0:
            x, y, k = request[req_id]
            ans = a[x+(pos-y)]
        else:
            ans = b[pos]
        sys.stdout.write(f'{ans}\n')

# inf.close()