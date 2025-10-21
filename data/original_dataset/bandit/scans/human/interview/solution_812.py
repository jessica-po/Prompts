import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(x)

n = int(input())
arr = sorted([(j, i + 1) for i, j in enumerate(map(int, input().split()))])

if n <= 3:
  print(arr[0][1])
  return


a1, a2, a3 = arr[0][0], arr[1][0], arr[2][0]
c1, c2, c3 = a3 - a2, a3 - a1, a2 - a1

flag = True
x = a2
for i in range(n):
  if i == 0:
    continue 
  if arr[i][0] != x:
    flag = False 
    break
  else:
    x += c1

if flag:
  print(arr[0][1])
  return

flag = True
x = a1
for i in range(n):
  if i == 1:
    continue 
  if arr[i][0] != x:
    flag = False 
    break
  else:
    x += c2

if flag:
  print(arr[1][1])
  return


flag = []
x = a1
for i in range(n): 
  if arr[i][0] != x:
    flag.append(arr[i]) 
  else:
    x += c3

if len(flag) >= 2:
  print(-1)
else:
  print(flag[0][1])