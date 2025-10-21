n = int(input())
s = input().split(':')
if n == 12:
    if s[0] == '00':
        s[0] = '01'
    elif int(s[0]) > 12 and s[0][1] == '0':
        s[0] = '10'
    elif int(s[0]) > 12:
        s[0] = '0' + s[0][1]
else:
    if int(s[0]) > 23:
        s[0] = '0' + s[0][1]
if int(s[1]) > 59:
    s[1] = '0' + s[1][1]
print(':'.join(s))