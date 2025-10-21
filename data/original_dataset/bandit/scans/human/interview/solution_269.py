s = input()
n = len(s)
t = 'RBYG'
for i in t:
	ind = s.find(i) % 4
	ans = 0
	while ind < n:
		ans += s[ind] == '!'
		ind += 4
	print(ans, end=' ')