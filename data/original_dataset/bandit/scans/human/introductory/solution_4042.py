r=float(input())
a=0
h=0
for i in range(1,11):
    for j in range(1,11):
        c=pow(j*j+i*i/4.,0.5)
        rtest=i*j*0.5/c
        if abs(rtest-r)<0.00001:
            a=i
            h=j
print(a,h)