from sys import stdin,stdout
input=stdin.readline
print=stdout.write
m,v=map(int,input().split())
a=[]
t=0
for i in range(m):
 x,y=map(int,input().split())
 a.append([x,y])
a.sort()
d=0
re=0
equip=0
for x,y in a:
 if d<x:
  d=x
  if y<=v:
   equip+=y
   re=v-y
   if y==v:
    d+=1
    re=0
  elif y>v and y<2*v:
   equip+=y
   d+=1
   re=2*v-y
  else:
   equip+=2*v
   d+=2
   re=0
 elif d==x:
  if re==0:
   if y<=v:
    equip+=y
    re=v-y
    if y==v:
     d+=1
     re=0
   elif y>=v and y<2*v:
    equip+=y
    d+=1
    re=2*v-y
   else:
    equip+=2*v
    d+=2
    re=0
  else:
   if y<re:
    equip+=y
    re-=y
   elif y==re:
    equip+=y
    re=0
    d+=1
   elif y>re:
    d+=1
    equip+=re
    y-=re
    if y<v:
     equip+=y
     re=v-y
    elif y>=v:
     equip+=v
     re=0
     d+=1
 elif d==x+1:
  if re==0:
   if y<v:
    equip+=y
    re=v-y
   elif y>=v:
    equip+=v
    re=0
    d+=1
  else:
   if y<=re:
    equip+=y
    re-=y
    if re==0:d+=1
   elif y>re:
    equip+=re
    re=0
    d+=1
print(str(equip))