a,b,c = map(int,input().split())

mod = a % b
ans = 'NO'
for i in range(1,b):  
  if (i*mod) % b == c:
    ans = 'YES'
    break
  
print(ans)