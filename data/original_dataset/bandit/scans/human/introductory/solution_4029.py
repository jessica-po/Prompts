import sys
import queue

INFINITY = 10**10

def main():
    n = input()
    print(solve(n))


def solve(n):
    if int(n) < 1000:
        return brute(n)
        
    forward = min([calc(str(n), last_digits) for last_digits in ["00", "25", "50", "75"]])
    reverse = min([calc(str(n), last_digits) + 1 for last_digits in ["52", "05", "57"]])
    res = min(forward, reverse)
    
    if res >= INFINITY:
        res = -1
    
    return res


def calc(n, last_digits):
    if not last_digits:
        return 0
    
    idx = n.rfind(last_digits[-1])
    if idx == -1:
        return INFINITY
    
    res = len(n) - idx - 1
    n = n[:idx] + n[(idx+1):]
    last_digits = last_digits[:-1]
    
    extra = 0
    if n and n[0] == '0':
        idx = len(n)
        for digit in "123456789":
            if n.find(digit) != -1:
                idx = min(idx, n.find(digit))
        
        if idx == len(n):
            return idx
        
        n = swap(n, 0, idx)
        extra = idx
    
    return res + calc(n, last_digits) + extra


def brute(n):
    q = queue.Queue()
    dis = dict()
    
    q.put(str(n))
    dis[str(n)] = 0
    
    while not q.empty():
        s = q.get()
        if int(s) % 25 == 0:
            return dis[s]
        
        for i in range(1, len(s)):
            j = i - 1
            t = swap(s, i, j)
            
            if t not in dis and t[0] != '0':
                dis[t] = dis[s] + 1
                q.put(t)
    
    return -1


def swap(s, i, j):
    chars = list(s)
    chars[i], chars[j] = chars[j], chars[i]
    return "".join(char for char in chars)


def __starting_point():
    main()

__starting_point()