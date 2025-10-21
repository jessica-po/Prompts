import sys

readline=sys.stdin.readline

s=list(readline().strip())
n=len(s)
f=n%2
mid=s[n//2]

for i in range(n//2):
  if s[n//2-i-1]!=mid or s[(n+1)//2+i]!=mid:
    print(((n+1)//2+i))
    break
else:
  print(n)