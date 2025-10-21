n,pos= (int(x) for x in input('').split())
s = input('')

def dis(a, b):
    a=ord(a)
    b=ord(b)
    return min(abs(a - b), abs(a+26-b), abs(b+26-a))

d = [dis(s[i], s[len(s)-i-1]) for i in range((len(s) + 1)//2)]
pos -= 1
if pos >= (len(s) + 1) // 2:
    pos = len(s) - pos - 1
#print(pos)

#print(d)
for rightmost, v in enumerate(reversed(d)):
    if v!=0:
        rightmost = len(d) - rightmost - 1
        break
for leftmost, v in enumerate(d):
    if v!=0:
        break
#print(leftmost, rightmost)
ans = min(abs(rightmost - pos) + rightmost - leftmost, abs(pos - leftmost) + rightmost - leftmost) + sum(d)
if sum(d) == 0:
    print(0)
else:
    print(ans)