x=int(input())
l=list(map(int, input().split(' ')))
l.sort()
a=1
for i in l:
    if i>=a:
        a+=1
print(a)