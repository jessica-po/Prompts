import math, sys

def mp():
    return list(map(int, input().split()))

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        print(x // 2)

deb = 0
if deb:
    file = open('input.txt', 'w')
else:
    input = sys.stdin.readline
    
main()