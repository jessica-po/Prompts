N = int(input())
v = sorted(map(int, input().split()))

tmp = v[0]
for i in range(1,N):
  tmp = (tmp+v[i])/2.0
  
print(tmp)