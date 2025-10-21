# cook your dish here
n = int(input())
l = list(map(int, input().strip().split()))
m = 0
f = []
for e in l:
 if(e != 0):
  m = m+1
 else:
  f.append(m)
  m = 0
 f.append(m)
print(max(f))