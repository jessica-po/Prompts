class Ortree():
    def __init__(self, n, As):
        size = 1
        while n > size:
            size *= 2
        self.size = size
        data = [0] * size + As[:] + [0] * (size - n)
        for idx in range(self.size - 1, 0, -1):
            idx2 = idx << 1
            data[idx] = data[idx2] | data[idx2 + 1]
        self.data = data
    
    def update(self, idx, val):
        pos = idx + self.size
        self.data[pos] = val
        pos >>= 1
        while pos:
            pos2 = pos << 1
            self.data[pos] = self.data[pos2] | self.data[pos2 + 1]
            pos >>= 1
        return self.data[1]


def solve(n, k, x, As):
    As.sort(reverse= True)
    xk = x**k
    if n == 1:
        As[0] *= xk
        return As[0]
    if is_simplecase(xk, As):
        As[0] *= xk
        return cumor(As)
    return complexcase(n, xk, As)
    

def cumor(As):
    result = 0
    for a in As:
        result |= a
    return result

def is_simplecase(xk, As):
    len0 = len(bin(As[0] * xk))
    len1 = len(bin(As[1] * xk))
    return len0 > len1

def complexcase(n, xk, As):
    len0 = len(bin(As[0] * xk))
    for i, a in enumerate(As[1:], 1):
        if len(bin(a * xk)) < len0:
            end = i
            rest = cumor(As[end:])
            break
    else:
        end = n
        rest = 0
    ortree = Ortree(end, As[:end])
    record = rest
    for i in range(end):
        score = ortree.update(i, As[i] * xk) | rest
        if record < score:
            record = score
        ortree.update(i, As[i])
    return record

n, k, x = map(int, input().split())
As = list(map(int, input().split()))
print(solve(n, k, x, As))