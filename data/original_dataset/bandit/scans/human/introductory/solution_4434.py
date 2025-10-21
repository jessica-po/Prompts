a=int(input())

for ufui in range(a):
    val=int(input())

    num=val//2 + 1
    count=0

    for i in range(num):
        count=count+i*((2*i+1)**2 - (2*i-1)**2)

    print (count)