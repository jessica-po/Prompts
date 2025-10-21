# coding: utf-8
n = int(input())
a = []
b = []
c = []
for i in input().split():
    i = int(i)
    if i < 0:
        a.append(i)
    elif i == 0:
        b.append(i)
    else:
        c.append(i)
if len(c) == 0:
    c.append(a.pop())
    c.append(a.pop())
if len(a)%2==0:
    b.append(a.pop())
print(len(a),' '.join([str(i) for i in a]))
print(len(c),' '.join([str(i) for i in c]))
print(len(b),' '.join([str(i) for i in b]))