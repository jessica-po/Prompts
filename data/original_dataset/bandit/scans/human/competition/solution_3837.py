from sys import stdin
import heapq

n,m,s = [int(x) for x in stdin.readline().split()]

bugs = [int(x) for x in stdin.readline().split()]
bugs = sorted([(bugs[x],x) for x in range(m)])

order = [x[1] for x in bugs]
bugs = [x[0] for x in bugs]

students = [int(x) for x in stdin.readline().split()]
rate = [int(x) for x in stdin.readline().split()]

valid = False
for x in range(n):
  if students[x] >= bugs[-1] and rate[x] <= s:
    valid = True
if not valid:
  print('NO')
else:
  print('YES')
  #print(students)
  for i,x in enumerate(students):
    low = 0
    high = m-1
    while high >= low:
      mid = (high+low)//2
      if bugs[mid] > x:
        high = mid-1
      else:
        low = mid+1
    #print(x,high)
    students[i] = high
  
  students = sorted([(students[x]+1,rate[x], x+1) for x in range(n)],reverse=True)
  #print(students)
  l1 = 1
  high = m

  lastValid = []
  lastD = 100000
  
  while l1 <= high:
    mid = (l1+high)//2
    shift = (mid-(m%mid))%mid
    segs = m//mid
    if shift > 0:
      segs += 1
    ind = 0
    q = []

    total = 0

    group = []

    for x in range(segs,0,-1):
      while ind<n:
        if (students[ind][0]+shift)//mid >= x:
          heapq.heappush(q,(students[ind][1],students[ind][2]))
          ind += 1
        else:
          break
      if q:
        r,i = heapq.heappop(q)
        group.append((x,i))
        total += r
      else:
        break
    if len(group) == segs and total <= s:
      #print(mid,total)
      high = mid-1
      lastValid = group
      lastD = mid
    else:
      l1 = mid+1
  complete = [0 for x in range(m)]
  lastValid.sort()
  mid = lastD
  shift = (mid-(m%mid))%mid
  skill = 1
  for bruh,i in lastValid:
    end = skill*mid-shift
    start = max(0,end-mid)
    for x in range(start,end):
      complete[x] = i
    skill += 1
  c2 = [0 for x in range(m)]
  for i,x in enumerate(complete):
    c2[order[i]] = x
  print(' '.join([str(x) for x in c2]))