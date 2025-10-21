import sys


#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

n, m = [int(i) for i in input().split()]
first = min(n, m)
second = (max(n, m) - first) // 2
print(first, second)