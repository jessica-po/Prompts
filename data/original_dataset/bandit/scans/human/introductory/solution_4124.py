s = input()[::-1]
t = input()[::-1]
i = 0
while i < min(len(s),len(t)) and s[i] == t[i]:
    i += 1
print(len(s) - i + len(t) - i)