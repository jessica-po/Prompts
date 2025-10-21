def chk(l):
	for i in range(4):
		for j in range(2):
			if l[i][j]==l[i][j+1]==l[i][j+2]=='x':
				return True
	for i in range(2):
		for j in range(4):
			if l[i][j]==l[i+1][j]==l[i+2][j]=='x':
				return True
	for i in range(2):
		for j in range(2):
			if l[i][j]==l[i+1][j+1]==l[i+2][j+2]=='x':
				return True
	for i in range(2):
		for j in range(2, 4):
			if l[i][j]==l[i+1][j-1]==l[i+2][j-2]=='x':
				return True
	return False
a = [list(input()), list(input()), list(input()), list(input())]
for i in range(4):
	for j in range(4):
		if a[i][j] != '.':
			continue
		a[i][j]='x'
		if chk(a):
			print("YES"); return
		a[i][j]='.'
print("NO")