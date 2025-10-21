from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    a,b,n = map(int,input().split())
    kroki = 0
    while max(a,b) <= n:
        if a > b:
            a,b = b,a
        a = a+b
        kroki += 1
    print(kroki)