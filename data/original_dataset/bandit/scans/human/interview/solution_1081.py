n = int(input())
s = {1, 7, 9, 10, 11}
if n < 12:
	if n in s:
		print("NO")
	else:
		print("YES")
elif 12 < n < 30:
	print("NO")
elif 69 < n < 80:
	print("NO")
elif 89 < n:
	print("NO")
else:
	if n % 10 not in {1, 7, 9}:
		print("YES")
	else: print("NO")