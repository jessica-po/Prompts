import sys

s = input()
all = s.split()

ans = "lol"
n = int(all[2])
x = float(all[0])
y = float(all[1])

a = 0
b = 1
dif = x / y
for i in range(1, n + 1):
    #print(str(a) + " : " + str(b) + " : " + str(dif))
    na = int((x * i) / y)
    if (dif > (abs(x * i - na * y) / (y * i))):
        a = na
        b = i
        dif = abs(x * i - na * y) / (y * i)
    na = na + 1
    if (dif > (abs(x * i - na * y) / (y * i))):
        a = na
        b = i
        dif = abs(x * i - na * y) / (y * i)
    #print(str(a) + " : " + str(b) + " : " + str(dif))
ans = str(a) + "/" + str(b)
    #print (a / b)
print(ans)