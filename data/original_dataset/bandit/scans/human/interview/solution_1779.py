s1 = input()
s2 = input()
s = input()
r=''
for i in s:
    if i.isalpha():
        #print (s1.index(i.lower()))
        if i.isupper():
            r+= (s2[(s1.index(i.lower()))].upper())
        else:
            r+=(s2[(s1.index(i.lower()))])
    else:
        r+=(i)
print (r)