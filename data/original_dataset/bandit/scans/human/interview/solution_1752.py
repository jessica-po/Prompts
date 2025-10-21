n = int(input())
a = list(map(int,input().split()))
a = sorted(a)

out = [0 for x in range(n)]
if n%2:
    out[n//2] = a[-1]
for x in range(n//2):
    out[x] = a[x*2]
    out[-(1+x)] = a[(x*2)+1]
print (" ".join(str(c) for c in out))