n = int(input())
s = input()
t = ''
lst = '1'
for i in s:
	if lst == '1':
		lst = i
		nw = ''
	else:
		if lst != i:
			t += lst
			t += i
			lst = '1'
print (len(s) - len(t))
print (t)