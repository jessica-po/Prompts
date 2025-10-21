import sys
import math

n = int(sys.stdin.readline())
if n <= 2:
  print(1)
  return

a = [int(s) for s in sys.stdin.readline().split()]

st = -1 # index of first positive number in current subset of a
ed = -1 # index last positive number in current subset of a 
        # differation is (a[ed] - a[st])/(ed - st)
leading_zeros = 0 # -1 before a[st]
seg_count = 1

for (i, v) in enumerate(a):
  if v == -1:
    if st == -1:
      leading_zeros += 1
    else:
      if ed != -1:
        # check if v should be a non-positive number
        if a[ed] + (i-ed) * (a[ed] - a[st])/(ed-st) <= 0:
          st = -1
          ed = -1
          leading_zeros = 1
          seg_count += 1
        else:
          pass
      else:
        pass
  else:
    if st == -1:
      st = i # find first positive number
    else:
      if ed == -1:
        ed = i
        #print(i)
        if (v - a[st]) % (i-st) != 0 or a[st] - (v-a[st])/(i-st) * leading_zeros <= 0:
          # a[st..i] can't be an arithmetic progression
          st = i
          ed = -1
          seg_count += 1
          leading_zeros = 0
        else:
          ed = i
      else:
        if (v-a[ed])%(i-ed) != 0 or (v-a[ed]) * (ed - st) != (a[ed] - a[st]) * (i-ed):
          st = i
          ed = -1
          seg_count += 1
          leading_zeros = 0
        else:
          ed = i #leave ed the first positive number after a[st] is also ok
  #print( "[" +str(st) + " " + str(ed) + "] " + str(seg_count) + " " + str(leading_zeros) )

print(seg_count)