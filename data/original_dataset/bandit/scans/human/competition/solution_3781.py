import sys
input=sys.stdin.readline
from collections import defaultdict

def solve(n,A):
    d=defaultdict(int)
    for a in A:
        d[a]+=1
    flag=True
    for v in d.values():
        if v%2!=0:
            flag=False
            break
    return bool(n%2)^flag

def main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        A=list(map(int,input().split()))
        judge=solve(n,A)
        print('Second' if judge else 'First')
    
def __starting_point():
    main()
__starting_point()