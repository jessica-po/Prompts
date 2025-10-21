n = int(input())
s = list(input())
for a in range(len(s)):
    s[a] = chr(ord(s[a]) + n)
    if ord(s[a])>90:
        s[a] = chr(ord(s[a])-26)
c=s[0]
for b in range(len(s)-1):
    c = c + s[b+1]
print(c)