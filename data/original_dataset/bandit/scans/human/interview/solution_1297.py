s=input()
result=0
sub=0
last=s[0]
for x in s:
     if x==last: sub+=1
     else:
          if sub%2==0: result+=1
          sub=1
     last=x

if sub%2==0: result+=1
print(result)