N = int(input())
A = list(map(int,input().split()))
if min(A) >= 0:
  Flag = True
elif max(A) <= 0:
  Flag = False
else:
  p_max = max(A)
  m_max = min(A)
  if abs(p_max) >= abs(m_max):
    Flag = True
  else:
    Flag = False
if Flag:
  MAX = max(A)
  for i,v in enumerate(A):
    if v == MAX:
      MAX_loc = i
      break
  ans = []; t = 0
  for i in range(N-1):
    if A[i+1] >= A[i]:
      continue
    A[i+1] += 2*MAX
    ans.append([MAX_loc+1,i+1+1])
    ans.append([MAX_loc+1,i+1+1])
    t += 2
    MAX_loc = i+1
    MAX = A[i+1]

else:
  MIN = min(A)
  for i, v in enumerate(A):
    if v == MIN:
      MIN_loc = i
      break
  ans = []; t = 0
  for i in range(N-1):
    if A[N-1-i] >= A[N-2-i]:
      continue
    A[N-2-i] += 2*MIN
    ans.append([MIN_loc+1,N-2-i+1])
    ans.append([MIN_loc+1,N-2-i+1])
    t += 2
    MIN_loc = N-2-i
    MIN = A[N-2-i]
print(t)
for x in ans:
  print((*x))
#print(ans,t,A)