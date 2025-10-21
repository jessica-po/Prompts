# cook your dish here
from sys import stdin, stdout
import math
# from itertools import permutations, combinations
from collections import defaultdict,deque
# import bisect
# import heapq as hq

def bfs(d,n,d1,s):
 high=[-1 for x in range(n+1)]
 q=deque([0])
 high[0]=0
 while q:
  node=q.popleft()
  for x in d1[int(s[node])]:
   if high[x]==-1:
    high[x]=high[node]+1
    q.append(x)
  for x in d[node]:
   if high[x]==-1:
    high[x]=high[node]+1
    q.append(x)
 print(high[n])
def main():
 try:
  s=stdin.readline().strip()
  n=len(s)
  d=defaultdict(list)
  
  for i in range(1,len(s)):
   d[int(s[i])].append(i)

  high=[0]*(n+1)
  visit=[False] *(n+1)
  q=deque([0])
  while q:
   node=q.popleft()
   if node==n-1:
    break
   for x in d[int(s[node])]:
    if visit[x]==False:
     visit[x]=True
     q.append(x)
     high[x]=high[node]+1
   d[int(s[node])].clear()
   if node-1>=0 and not visit[node-1]:
    visit[node-1]=True
    q.append(node-1)
    high[node-1]=high[node]+1
   if node+1<n and not visit[node+1]:
    visit[node+1]=True
    q.append(node+1)
    high[node+1]=high[node]+1
  print(high[n-1])
 except:
  pass
 
def add(a, b, c):
 res = a + b;
 if (res >= c):return res - c;
 else:return res;
def mod(a, b, c):
 res = a * b
 if (res >= c):return res % c
 else:return res
def gcd(a, b):
 while b:
  a, b = b, a % b
 return a
def lcm(a, b):
 w = a // gcd(a, b)
 return w * b
def expo(a, b):
 x, y = 1, a
 while (b > 0):
  if (b & 1):
   x = x * y
  y = y * y
  b >>= 1
 return x
def power(a, b, m):
 x, y = 1,
 while (b > 0):
  if (b & 1):x = mod(x, y, m)
  y = mod(y, y, m)
  b >>= 1
 return x
def L():
 return list(map(int, stdin.readline().split()))
def In():
 return list(map(int, stdin.readline().split()))
def I():
 return int(stdin.readline())
P = 1000000007

def __starting_point():
 main()



__starting_point()