s = input()
pref = []
cnt1 = s.count('1')
s = s.replace('1', '')
i = 0
while i < len(s) and s[i] != '2':
	i += 1
end = ''
if i != len(s):
	end = s[i:]
s = s[:i] + '1' * cnt1 + end
print(s)