import operator
N = eval(input());
N = int(N);
k = eval(input());
k = int(k);
list= [];
for i in range(k):
 a=eval(input());
 a=int(a);
 list.append(a);
list.sort() 
for i in range(k,N):
 a=eval(input())
 a=int(a)
 if(a>=0):
  if(a<list[k-1]):
    list.pop()
    list.append(a)
    list.sort()
 else:
    print(list[k-1])