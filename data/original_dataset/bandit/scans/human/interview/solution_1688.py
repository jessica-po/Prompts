#TO MAKE THE PROGRAM FAST

''' ----------------------------------------------------------------------------------------------------  '''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque
''' ----------------------------------------------------------------------------------------------------  '''




#FOR TAKING INPUTS

''' ----------------------------------------------------------------------------------------------------  '''
def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def val():return int(input().rstrip('\n'))
def st():return input().rstrip('\n')
def sttoli():return [int(i) for i in input().rstrip('\n')]
''' ----------------------------------------------------------------------------------------------------  '''




#MAIN PROGRAM

''' ----------------------------------------------------------------------------------------------------  '''

d = deque()
n = val()
l = li()
j = x = 0
currmax = -10000000000000
ans = []
for i in range(n):
    while len(d) and d[0] < i:d.popleft()
    currmax = l[d[0]%n] if len(d) else l[i]
    while j<3*n:
        currmax = max(currmax,l[j%n])
        while len(d) and l[d[-1]%n] <= l[j%n]:d.pop()
        d.append(j)
        if currmax/2 > l[j%n]:
            ans.append(j-i)
            break
        j += 1
    if j == 3*n:
        print(*([-1 for _______ in range(n)]))
        return
print(*ans)





''' ----------------------------------------------------------------------------------------------------  '''