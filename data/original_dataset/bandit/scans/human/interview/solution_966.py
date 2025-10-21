def find(ins):
	ins += 1
	
	test = [int(i) for i in str(ins)]
	
	inlist = []
	
	for i in test:
		if i in inlist:
			
			test = find(ins)
			break
			
		else:
			inlist.append(i)
	
	return ''.join(str(x) for x in test)
	
ins = int(input())
print(find(ins))