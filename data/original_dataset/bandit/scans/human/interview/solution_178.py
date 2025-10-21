n, s = int(input()), input()
cnt = (n - 11) // 2
cnt_8 = len(s[:n - 10].split('8')) - 1
if (cnt >= cnt_8):
	print ("NO")
else:
	print ("YES")