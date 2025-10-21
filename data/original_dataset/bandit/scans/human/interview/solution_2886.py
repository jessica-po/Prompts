import sys
s = input()
l = len(s)
if l == 2:
    if s[0] == s[1]:
        print(1, 2)
        return
    else:
        print('-1 -1')
        return
for i in range(l - 2):
    s1 = s[i]
    s2 = s[i + 1]
    s3 = s[i + 2]
    if s1 == s2 or s1 == s3 or s2 == s3:
        print(i + 1, i + 3)
        return
print('-1 -1')