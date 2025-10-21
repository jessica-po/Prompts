bad = ['e', 'a', 'i', 'o', 'u', 'y']

n = int(input())
s = input()
ans = ''
i = 0
while i != len(s):
    if s[i] in bad:
        letter = s[i]
        pos = i
        while i != len(s) and letter == s[i]:
            i += 1
        if i - pos == 2 and letter in ['e', 'o']:
            ans += 2 * letter
        else:
            ans += letter
    else:
        ans += s[i]
        i += 1
print(ans)