string = input()
l = string.split(" ")
n, m, k = int(l[0]),int(l[1]),int(l[2])
l = [{(1,1),}]
count = 1
In = 0
while count < k:
	s = set()
	for i in l[In]:
		x = i[0]+1
		y = i[1]
		if x<=n and y<=m:
			t = [0,0]
			t[0],t[1] = x, y
			s.add(tuple(t))
		x = i[0]
		y = i[1]+1
		if x<=n and y<=m:
			t = [0,0]
			t[0],t[1] = x, y
			s.add(tuple(t))
	l.append(s)
	In+=1
	count+=len(l[In])
l2 = []
Count = 0
flag = 0
for i in l:
	for h in i:
		if Count==k:
			flag = 1
			break
		l3 = [h]
		x,y = h[0],h[1]
		while x!=1 or y!=1:
			if x>y:
				x-=1
				l3.append((x,y))
			else:
				y-=1
				l3.append((x,y))
		l2.append(l3)
		Count+=1
	if flag==1:
		break

cost = 0
string = ""
for i in range(k):
	length = len(l2[k-i-1])
	cost+=length
	for j in range(length):
		t = l2[k-i-1][length - j - 1]
		x,y = t[0],t[1]
		string += "("+str(x)+","+str(y)+") "
	string += "\n"
	
print(cost)
print(string)