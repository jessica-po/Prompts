x = int(input())
y = list(map(int, input().split(' ')))
if y == [0] * x:
    print(0)
    quit()
for i in range(x):
    if y[i] == 1:
        y = y[i:]
        break

y.reverse()
for i in range(len(y)):
    if y[i] == 1:
        y = y[i:]
        break

y.reverse()

l = []
ct = 0
for i in y:
    if i == 0:
        ct+=1
    if i == 1 and ct != 0:
        l.append(ct)
        ct = 0

k = 1
for i in l:
    k *= (i+1)

print(k)