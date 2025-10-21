n = int(input())
s = input()
j = 1
result = []
for i in range(n):
    while (j < n-1) and (s[i:j] in s[j:]):
        j += 1
    result.append(j-i-1)
print(max(result))