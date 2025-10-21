s = input().strip()
if len(s)<=2:
    print(s)
    return
ne = s[0]+s[1]
for i in range(2,len(s)):
    if s[i]!=s[i-1] or s[i]!=s[i-2]:
        ne+=s[i]
ne2 = ne[:3]
for i in range(3,len(ne),1):
    if ne2[-3]==ne2[-2] and ne2[-1]==ne[i]:
        pass
    else:
        ne2+=ne[i]
print(ne2)