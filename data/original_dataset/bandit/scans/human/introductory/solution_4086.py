n=int(input())
ar=list(map(int,input().split()))
s=set()
a=[]
for x in ar[::-1]:
    if x not in s:
        a.append(x)
    s.add(x)
print(len(a))
print(*a[::-1])