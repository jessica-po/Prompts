n = int(input())
shows = []
for i in range(n):
  l, r = map(int, input().split())
  shows.append((l,r))
  
shows.sort()

a_endtime, b_endtime = -1, -1
for show in shows:
  if show[0] <= a_endtime:
    print('NO')
    break
  else:
    a_endtime = show[1]
    if a_endtime > b_endtime:
      a_endtime, b_endtime = b_endtime, a_endtime
  
else:
  print('YES')