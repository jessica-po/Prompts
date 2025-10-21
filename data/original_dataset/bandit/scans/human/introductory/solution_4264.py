n=input()

count=0
for i in range(1,int(n)+1):
  l=len(str(i))
  if l%2!=0:
    count+=1
print(count)