k = int(input())
a = reversed(input())
b = reversed(input())

aa = [0] * (k + 1)
bb = [0] * (k + 1)
for i, x in enumerate(a):
    aa[i] = ord(x) - 97
for i, x in enumerate(b):
    bb[i] = ord(x) - 97

carry = 0
cc = [0] * (k + 1)
for i in range(k + 1):
    cc[i] = aa[i] + bb[i] + carry
    if cc[i] >= 26:
        carry = 1
        cc[i] -= 26
    else:
        carry = 0

carry = 0
for i in reversed(list(range(k+1))):
    value = carry * 26 + cc[i]
    carry = value % 2
    cc[i] = value // 2

answer = ""
for x in reversed(cc[:-1]):
    answer += chr(x + 97)
print(answer)