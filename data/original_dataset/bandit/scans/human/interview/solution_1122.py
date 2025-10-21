N,M=map(int,input().split())

if M%2==0:
  for i in range(M//2):
    print(i+1,M-i)
  for i in range(M//2):
    print(M+i+1,2*M-i+1)  
else:
  for i in range(M//2):
    print(i+1,M-i)
  for i in range(M//2+1):
    print(M+i+1,2*M-i+1)