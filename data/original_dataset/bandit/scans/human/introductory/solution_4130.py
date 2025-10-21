n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
s=set()
for val in arr:
  if val!=1 and val-1 not in s:
      s.add(val-1)
  elif val not in s:
    s.add(val)
  elif val+1 not in s:
    s.add(val+1)
print(len(s))