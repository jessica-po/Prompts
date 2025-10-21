hola = 0
a = int(input())
d = len(str(a))
k = 10**(d-1)
for i in range(1, d):
    hola += i * (10**(i-1)*9)

hola += d * (a-k+1)
print(hola)