s = input()
m = int(input())
mn = m
ttt = 0
t = 0
ttt = 1
for i in range(1,len(s)):
    ttt = (ttt * 10) % m
for i in range(0,len(s)):
    t = (t * 10 + ord(s[i]) - ord('0')) % m
for i in range(0,len(s)):
    if s[i] != '0':
        mn = min(mn,t)
    t = t - (((ord(s[i])- ord('0')) * ttt) % m)
    if t < 0:
        t = t + m
    t = (t * 10 + (ord(s[i])- ord('0'))) % m
print(mn)