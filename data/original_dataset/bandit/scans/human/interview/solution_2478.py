n=int(input())
S=input()
x=y=0
for i,s in enumerate(S):
  y=y-1 if s=='(' else y+1
  x=max(x,y)
print('('*x+S+')'*(x-y))