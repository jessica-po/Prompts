l=list(map(int,input().split()))
l.insert(0,0)
c1=[1,6,3,8,5,10,7,12,9,23,11,21,13,14,15,16,17,18,19,20,4,22,2,24]
c2=[1,23,3,21,5,2,7,4,9,6,11,8,13,14,15,16,17,18,19,20,12,22,10,24]
c3=[1,2,3,4,5,6,15,16,9,10,11,12,13,14,23,24,17,18,7,8,21,22,19,20]
c4=[1,2,3,4,5,6,19,20,9,10,11,12,13,14,7,8,17,18,23,24,21,22,15,16]
c5=[1,2,16,14,5,6,7,8,19,17,11,12,13,9,15,10,3,18,4,20,21,22,23,24]
c6=[1,2,17,19,5,6,7,8,14,16,11,12,13,4,15,3,10,18,9,20,21,22,23,24]
flag=0
mark=0
for i in range(6):
	if(l[c1[4*i]] == l[c1[4*i+1]] == l[c1[4*i+2]] == l[c1[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

mark=0
for i in range(6):
	if(l[c2[4*i]] == l[c2[4*i+1]] == l[c2[4*i+2]] == l[c2[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

mark=0
for i in range(6):
	if(l[c3[4*i]] == l[c3[4*i+1]] == l[c3[4*i+2]] == l[c3[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

mark=0
for i in range(6):
	if(l[c4[4*i]] == l[c4[4*i+1]] == l[c4[4*i+2]] == l[c4[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

mark=0
for i in range(6):
	if(l[c5[4*i]] == l[c5[4*i+1]] == l[c5[4*i+2]] == l[c5[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

mark=0
for i in range(6):
	if(l[c6[4*i]] == l[c6[4*i+1]] == l[c6[4*i+2]] == l[c6[4*i+3]]):
		mark=1
	else:
		mark=0
		break
if(mark):
	flag=1

if(flag):
	print("YES")
else:
	print("NO")