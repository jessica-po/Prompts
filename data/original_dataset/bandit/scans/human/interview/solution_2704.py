n,m=[int(x) for x in input().split()]
k=[int(x) for x in input().split()]
a=min(k)
b=max(k)
for i in range(m):
 c=int(input())
 if c>=a and c<=b:
  print('Yes')
 else:
  print('No')