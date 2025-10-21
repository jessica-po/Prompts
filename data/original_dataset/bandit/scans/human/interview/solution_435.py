n, k = map(int,input().split())
s = input()
maxi = 0
a = 0
b = 0
st = 0
for i in range(0, n):
    if s[i] == 'a': a += 1
    else: b+=1
    if min(a, b) > k:
        if s[st] == 'a': a-=1
        else: b-=1
        st += 1
    else: maxi += 1
print(maxi)