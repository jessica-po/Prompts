def readln(): return tuple(map(int, input().split()))

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, k = readln()
lst = [(v, i + 1) for i, v in enumerate(readln())]
lst.sort()
lst.reverse()
print(lst[k - 1][0])
print(*list(zip(*lst[:k]))[1])