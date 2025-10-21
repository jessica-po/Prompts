n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append('<')
    arr.append('3')
    for j in range(len(s)):
        arr.append(s[j])
arr.append('<')
arr.append('3')
s = input()
cur = 0
i = 0
while cur < len(s) and i < len(arr):
    if s[cur] == arr[i]:
        i+=1
    cur+=1
if i == len(arr):
    print('yes')
else:
    print('no')