# cook your dish here
t = int(input())
while t>0:
 x = input().split()
 n = int(x[0])
 k = int(x[1])
 ans = 0
 for i in range(n):
  if (k&(1<<i))!=0:
   ans += 2**(n-i-1)
 print(ans, end="\n") 
 t -= 1