# add 0,4,9,49
# this is a stupid solution

import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

# do a stupid approach
dp=[0]*150
s=set([0])
for i in range(150):
    dp[i]=len(s)
    s2=set(s)
    for j in s:
        s2.add(j+4)
        s2.add(j+9)
        s2.add(j+49)
    s=s2

if 0:
    for i in range(100):
        if dp[i+49]-dp[i]!=2401:
            print(i)

if n<150: print(dp[n])
else:
    stuff=(n//49)
    while n-stuff*49+49<150: stuff-=1
    print(dp[n-stuff*49]+2401*stuff)