s=input()
n=len(s)
p=0
for i in range(n):
  if s[i]=='p':
    p+=1
print(n//2-p)