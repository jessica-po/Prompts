#import sys

#fin = open("input.txt", 'r')
#fout = open("output.txt", 'w')

#fin = open("input.txt", 'r')
#fout = open("output.txt", 'w')

n = int(input())
a = list(map(int, input().split()))

if 1 not in a:
    print(1)
else:
    print(-1)