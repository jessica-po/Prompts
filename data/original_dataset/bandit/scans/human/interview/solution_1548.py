n = int(input())
l = list(map(int,input().split()))
l.sort()
a = l[:n//2]
b = l[n//2:]
print(sum(a)**2+sum(b)**2)