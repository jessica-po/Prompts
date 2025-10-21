s = input()
d = dict()
d['V'] = 'K'
d['K'] = 'V'
m = s.count('VK')
s = list(s)
for i in range(len(s)):
    s[i] = d[s[i]]
    m = max(m,''.join(s).count('VK'))
    s[i] = d[s[i]]
print(m)