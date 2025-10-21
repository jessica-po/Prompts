from collections import Counter, defaultdict
import itertools
import sys

def main():
    n = int(input())
    spec = 3
    poss = True
    for _ in range(n):
        winner = int(input())
        if winner != spec:
            spec = 6 - winner - spec
        else:
            poss = False
    print('YES' if poss else 'NO')



main()