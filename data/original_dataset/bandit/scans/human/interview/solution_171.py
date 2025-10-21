s = input().strip()
flag1 = len(s) >= 5
d1 = 'qwertyuiopasdfghjklzxcvbnm'
d2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
d3 = '123456789'
flag2 = False
flag3 = False
flag4 = False

for i in d1:
    if i in s:
        flag2 = True
for i in d2:
    if i in s:
        flag3 = True
for i in d3:
    if i in s:
        flag4 = True  
if(flag1 and flag2 and flag3 and flag4):
    print("Correct")
else:
    print("Too weak")