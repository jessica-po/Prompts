import sys, math
s=input()
pal='AHIMOoTUVvWwXxY'
n=len(s)
l=0
r=n-1
flag=True
fir='pq'
sec='bd'
while l<=r:
    if s[l]==s[r] and s[l] in pal:
        l+=1
        r-=1
        continue
    elif s[l]==s[r]:
        flag=False
        break
    elif (s[l] in fir) and (s[r] in fir):
        l+=1
        r-=1
        continue
    elif (s[l] in sec) and (s[r] in sec):
        l+=1
        r-=1
        continue
    else:
        flag=False
        break
if flag:
    print('TAK')
else:
    print('NIE')