N=int(input())
l=[]
for i in range (N):
    a=input().split()
    l.append(a)
count = 0
for i in range(N):
    flag = 0
    value=l[i].count('T')
    for j in range (N):
     if l[i][j] =='T' and i!=j :
      if l[i] == l[j]:
       continue
      else:
       flag=1
       break
    if flag==0 and count<value:
     count=value
print(count)