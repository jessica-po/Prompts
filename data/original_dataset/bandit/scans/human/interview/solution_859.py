s=input()
t=input()
a=0
b=0
c=0
for i in range(len(s)):
   if s[i]=='+':a+=1
   else:a-=1
for i in range(len(t)):
   if t[i]=='+':b+=1
   elif t[i]=='-':b-=1
   else:c+=1
x=a-b
d=0-c
y=0-1
for i in range(c+1):
   if d==x:y=i
   d+=2

def fact(n):
   w=1
   for i in range(n):
      w*=(i+1)
   return(w)
  
def parmi(k,n):
   w=1
   w*=fact(n)
   w//=fact(k)
   w//=fact(n-k)
   return(w)
   
def puiss(k,n):
   w=1
   for i in range(n):
      w*=k
   return(w)
   
if y==-1:print(0.0)
else:print(parmi(y,c)/puiss(2,c))