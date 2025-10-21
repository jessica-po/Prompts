#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n,a,b = map(int,input().split())
    a_count=0
    d,r=divmod(n,a+b)
    a_count+=a*d
    if r > a:
        a_count+=a
    else:
        a_count+=r
    print(a_count)

def __starting_point():
    main()
__starting_point()