kk=0
x = int(input())
y = input()
z = [i for i in range(len(y)) if y[i] == '*']
for i in range(0, 100):
    for j in range(1, 100):
        if i in z and i+j in z and i+2*j in z and i+3*j in z and i+4*j in z:
            kk=1
if kk==1:
    print("yes")
else:
    print("no")