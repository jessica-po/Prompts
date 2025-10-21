q=str(input())
e=str(input())
a=len(q)
b=len(e)
c=""
if a==b:
  for i in range(a):
    c+=q[i]
    c+=e[i]
else:
  for i in range(b):
    c+=q[i]
    c+=e[i]
  c+=q[a-1]

print(c)