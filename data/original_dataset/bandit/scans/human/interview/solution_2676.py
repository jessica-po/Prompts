# cook your dish here
n=int(input())
l=[]
for i in range(n):
 l.append(input())
m=int(input())
s=input()
c=0
res=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
res=list(dict.fromkeys(res))
for i in res:
 if i in l:
  c=c+1
print(c)