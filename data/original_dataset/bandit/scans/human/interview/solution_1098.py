n = int(input())
a = []
for i in range(n):
	h, m = map(int, input().split(":"))
	a.append((h + 24) * 60 + m)
	a.append(h * 60  + m)
a.sort()
j = 0
s = 0
ans = 0
for i in range(0, 48 * 60):
	if (j < 2 * n and a[j] == i):
		ans = max(ans, s)
		s = 0
		j += 1
		continue
	else:
		s += 1
h = ans // 60
m = ans % 60
hans = ""
mans = ""
if h < 10:
	hans = "0" + str(h)
else:
	hans = str(h)
if m < 10:
	mans = "0" + str(m)
else:
	mans = str(m)
print(hans + ":" + mans)