read=lambda:list(map(int,input().split()))
from collections import Counter as co
k,n=read()
s=input()
repeated=(len(s)!=len(set(s)))
etalon=co(s)
a=[]
kk=[]
ap=a.append

for i in range(k-1):
    ap(input())
    if co(a[-1])!=etalon:
        print(-1)
        return

ss=False
for i in a:
    if i!=s:
        ss=i
        for j in range(len(s)):
            if s[j]!=ss[j]:
                kk.append(j)
        break

if len(kk)>4:
    print(-1)
    return

if ss:
    if repeated:
        for i in a:
            k = 0
            for j in range(len(i)):
                if s[j] != i[j]: k += 1
            if k != 0 and k != 2: break
        else:
            print(s)
            return

    if len(kk)!=2:
        for i in range(len(kk)):
            for j in range(i):
                stry=s[:kk[j]]+s[kk[i]]+s[kk[j]+1:kk[i]]+s[kk[j]]+s[kk[i]+1:]
                #print(stry)
                for u in a:
                    k = 0
                    for j in range(len(u)):
                        if stry[j] != u[j]: k += 1
                    #print(stry,i,k)
                    if not(k==0 and repeated) and k != 2: break
                else:
                    print(stry)
                    return

    if len(kk)==2:
        for change in kk:
            for i in range(len(s)):
                if change==i:
                    continue

                if i >change:
                    stry = s[:change] + s[i] + s[change + 1:i] + s[change] + s[i + 1:]
                else:
                    stry = s[:i] + s[change] + s[i + 1:change] + s[i] + s[change + 1:]

                for u in a:
                    k = 0
                    for j in range(len(u)):
                        if stry[j] != u[j]: k += 1
                    #print(stry,i,k)
                    if not(k==0 and repeated) and k != 2: break
                else:
                    print(stry)
                    return
    print(-1)

else:
    if repeated:
        print(s)
        return
    print(s[1]+s[0]+s[2:])