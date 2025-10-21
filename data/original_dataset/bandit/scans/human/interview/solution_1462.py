n, k = map(int, input().split())
arr = [0] * 26
s = input()
aux = ord('A')
for i in range(len(s)):
    arr[ord(s[i]) - aux] += 1
arr.sort(reverse = True)
i = 0
sum = 0
while k > 0:
    if arr[i] >= k:
        sum += k ** 2
        k = 0
    else:
        k -= arr[i]
        sum += arr[i] ** 2
        i += 1
print(sum)