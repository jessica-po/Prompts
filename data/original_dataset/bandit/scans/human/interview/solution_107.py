s = input()
i = 0
while i < len(s) and s[i] == '0':
    i += 1
cnt = 0
while i < len(s):
    if s[i] == '0':
        cnt += 1
    i += 1

if cnt >= 6:
    print('yes')
else:
    print('no')