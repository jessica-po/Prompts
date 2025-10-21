ct = 0
x = int(input())
y = list(map(int, input().split(' ')))
z = list(map(int, input().split(' ')))
for i in range(1, 720721):
    for j in range(x):
        if i%y[j] == z[j]:
            ct+=1
            break
print(ct/720720)