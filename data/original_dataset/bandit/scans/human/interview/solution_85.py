a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
e=a*b
f=c*d
n=0
while e%2==0:e=e//2
while e%3==0:e=e//3
while f%2==0:f=f//2
while f%3==0:f=f//3
if e!=f:print("-1")
else:
   i=0
   j=0
   e=a*b
   f=c*d
   while e%3==0:
      e=e//3
      i+=1
   while f%3==0:
      f=f//3
      j+=1
   k=i-j
   if k>0:
      for i in range(k):
         n+=1
         if a%3==0:a=a*2//3
         else:b=b*2//3
   else:
      for i in range(0-k):
         n+=1
         if c%3==0:c=c*2//3
         else:d=d*2//3
   e=a*b
   f=c*d
   i=0
   j=0
   while e%2==0:
      e=e//2
      i+=1
   while f%2==0:
      f=f//2
      j+=1
   k=i-j
   if k>0:
      for i in range(k):
         n+=1
         if a%2==0:a=a//2
         else:b=b//2
   else:
      for i in range(0-k):
         n+=1
         if c%2==0:c=c//2
         else:d=d//2
   print(n)
   print(a,b)
   print(c,d)