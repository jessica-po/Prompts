n,k,q = [int(x) for x in input().split()]
a = []
for i in range(q):
  a.append(int(input()))
res = [0] * n
for i in range(q):
  res[a[i]-1] += 1
b = q - k
#print(res)
for i in range(n):
  if res[i] > b:
    print("Yes")
  else:
    print("No")