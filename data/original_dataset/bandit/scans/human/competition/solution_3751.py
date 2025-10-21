s = input()

last = -1
for i in range(26):
	c = chr(ord('a') + i)
	kk = s.find(c)
	if kk == -1:
		kk = len(s)
	if kk < last:
		print("NO")
		return
	last = kk
print("YES")