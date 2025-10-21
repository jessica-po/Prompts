import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
#import numpy as np
def main():
    n = int(input())
    if n == 1:
        print((1))
        return
    r = 0
    for i1 in range(1, n + 1):
        num_of_div = n // i1
        r += num_of_div * (num_of_div + 1) // 2 * i1
    print(r)

def __starting_point():
    main()

__starting_point()