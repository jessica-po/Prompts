k = int(input())
n = input()
digit = [0]*10
for c in n:
    digit[int(c)]+= 1
dsum = sum(i*digit[i] for i in range(10))

i = 0
change = 0
while dsum < k:
    if digit[i] == 0:
        i+= 1
        continue
    digit[i]-= 1
    digit[9]+= 1
    change+= 1
    dsum+= 9-i
print(change)