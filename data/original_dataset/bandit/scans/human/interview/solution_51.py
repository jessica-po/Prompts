s = input()
t = 0
if len(s)%2==0:
    n = (len(s)-1)//2+1
else:
    n = (len(s)-1)//2
for i in range(n, len(s)-1):
    a = i
    b = len(s)-i-1
    if s[:a+1]==s[b:]:
        print('YES')
        print(s[:a+1])
        t = 1
        break
if t==0:
    print('NO')