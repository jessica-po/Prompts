import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

for a in range(1,n+1)[::-1]:
    if n%a: continue
    if a>n//a: continue
    print("%s %s"%(a,n//a))
    break