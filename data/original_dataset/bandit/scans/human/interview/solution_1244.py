n = int(input())
mas = list(map(int, input().split()))
mas2 = [0 for _ in range(1001)]
for i in mas:
    mas2[i]+=1
i = 0
for i in mas2:
    if i > (n + 1) / 2:
        print ("NO")
        return
print ("YES")