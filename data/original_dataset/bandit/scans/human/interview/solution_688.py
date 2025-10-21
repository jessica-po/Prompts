t1  = map(int,input().strip())
t2 = map(int,input().strip())
ar1 = [0] * 10
ar2  = [0]*10
for j in t1:
    ar1[j]+=1
for j in t2:
    ar2[j]+=1
ar1[2]+=ar1[5]
ar1[6]+=ar1[9]
ar1[5]=ar1[9]=0
ar2[2]+=ar2[5]
ar2[6]+=ar2[9]
ar2[5]=ar2[9]=0
print(int(min(map(lambda x:ar2[x]/ar1[x] if ar1[x]!=0 else 100500 ,range(10)))))