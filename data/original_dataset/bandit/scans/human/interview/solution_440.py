n = int(input())
s = input()
t = []
vowels = 'aeiouy'
for c in s:
    if t and t[-1] in vowels and c in vowels:
        continue
    else:
        t.append(c)
print(''.join(t))