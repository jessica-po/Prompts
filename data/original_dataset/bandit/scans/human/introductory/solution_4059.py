N = int(input())
ANS = 1
for i in range(1,N-1):
  ANS += (N-1)//i
  
print(ANS)