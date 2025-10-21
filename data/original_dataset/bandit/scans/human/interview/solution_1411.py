def bins(sortedlist,x):
    n=len(sortedlist)
    start = 0
    end = n - 1

    while(start <= end):
        mid =int( (start + end)/2)
        if (x == sortedlist[mid][0]):
            return mid
        elif(x < sortedlist[mid][0]):
            end = mid - 1
        else:
            start = mid + 1 
 
    if(sortedlist[mid][0]<=x):
        return mid
    else:
        return mid-1




n,s=list(map(int,input().split()))
hap=[]

for i in range(n):
    hap.append(list(map(int,input().split())))
a=0
max1=0
b=0
sla=[]
slb=[]
slab=[]
for i in range(n):
    temp=hap[i][0]
    hap[i][0]=hap[i][1]
    hap[i][1]=hap[i][2]
    hap[i][2]=temp
for i in range(n):

    slab.append([hap[i][0]-hap[i][1],hap[i][2]])
happi=0
for i in range(n):
    if(hap[i][0]>hap[i][1]):
        a+=hap[i][2]
        happi+=hap[i][2]*hap[i][0]
    else:
        b+=hap[i][2]
        happi+=hap[i][2]*hap[i][1]
sla.sort()
slb.sort()
slab.sort()
if((a%s +  b%s)>s):
    print(happi)
else:
    loc=bins(slab,0)
    happia=happi
    count=0
    #print(a,b)
    b=b%s
    a=a%s
    left=b%s
    
    while(left>0):
        if(slab[loc+count][1]<left):
            happia+=slab[loc+count][0]*slab[loc+count][1]
            left-=slab[loc+count][1]
        else:
            happia+=slab[loc+count][0]*left
            break
        count-=1
    left=a%s
    count=0
    happib=happi
    
    while(loc<n and slab[loc][0]<=0):
        loc+=1
    #print(slab[loc][0])
    while(left>0):
        if(slab[loc+count][1]<left):
            happib-=slab[loc+count][0]*slab[loc+count][1]
            left-=slab[loc+count][1]
        else:
            happib-=slab[loc+count][0]*left
            break
        count+=1
    #print(happia,happib,happi)
    print(max(happia,happib))