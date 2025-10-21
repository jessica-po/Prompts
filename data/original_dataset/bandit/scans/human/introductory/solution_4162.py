N = int(input())
a = list(map(int,input().split()))
aa = []
for i in a:
    aa.append(i-1)
print(sum(aa))