k = []

x = int(input())
c, d = list(map(int, input().split(' ')))
for i in range(x):
    a, b = list(map(int, input().split(' ')))
    k.append([c*a+b, d*a+b])

k.sort()
for i in range(len(k)-1):
    if k[i+1][1] < k[i][1]:
        print("YES")
        quit()
print("NO")