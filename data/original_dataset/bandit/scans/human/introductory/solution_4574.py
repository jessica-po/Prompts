n=int(input())
a=[int(i) for i in input().split()]


a.sort()

count=0


def get_num(a):
    count=1
    taishou = a.pop()
    while a!=[]:
        second=a.pop()
        if taishou==second:
            count+=1
        else:
            a.append(second)
            break
    if count==1:
        return taishou,0
    elif count==2 or count==3:
        return taishou,1
    else:
        return taishou,2

one=0
two=0


while a!=[] and (one==0 or two==0):
    hen,length=get_num(a)
    if length==1:
        if one==0:
            one=hen
        else:
            two=hen
    elif length==2:
        if one==0:
            one=hen
            two=hen
        else:
            two=hen

print((one*two))