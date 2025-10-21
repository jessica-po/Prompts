import sys; sys.setrecursionlimit(1000000)
def solve():
    n, m, = rv()
    s = list(input())
    res = [0] * m
    #replace dot:
    #dot had nothing on left or right: nothing changes
    #dot had one on left or right: -1
    #dot had two on left or right: -2

    #replace char:
    #if had two chars on left and right: 0
    # if had one char and one dot: +1
    # if had two dots: +2
    helper = list()
    for i in range(n):
        if s[i] == '.':
            if i == 0:
                helper.append(1)
            else:
                if s[i-1] == '.':
                    helper[-1] += 1
                else:
                    helper.append(1)
    initval = 0
    for val in helper:
        initval += val - 1
    for query in range(m):
        index, replace = input().split()
        index = int(index) - 1
        if (s[index] == '.' and replace == '.') or (s[index] != '.' and replace != '.'):
            res[query] = initval
        else:
            sidedots = 0
            if index > 0:
                if s[index - 1] == '.': sidedots+=1
            if index < n - 1:
                if s[index + 1] == '.': sidedots+=1
            if s[index] == '.':
                res[query] = initval - sidedots
                initval -= sidedots
            else:
                res[query] = initval + sidedots
                initval += sidedots
        s[index] = replace
    print('\n'.join(map(str, res)))




def rv(): return list(map(int, input().split()))
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()