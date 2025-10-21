am=0
x = int(input())
l = list(map(int, input().split(' ')))
m = min(l)
k = [i for i in range(x) if l[i] == m]
k.append(k[0]+x)
for i in range(len(k)-1):
    am = max(am, k[i+1]-k[i])

print(m * x + am - 1)