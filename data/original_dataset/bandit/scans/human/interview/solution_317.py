n = int(input())
s = input()
a = [False for i in range(26)]
for x in s:
    a[ord(x.lower()) - ord('a')] = True
for x in a:
    if not x:
        print('NO')
        return
print('YES')