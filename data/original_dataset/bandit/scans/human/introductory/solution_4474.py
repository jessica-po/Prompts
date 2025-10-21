for _ in range(int(input())):
	n = int(input())

	bits = ['1']
	while int(''.join(bits), 3) < n:
		bits.append('1')
	
	
	for i in range(len(bits)):
		bits[i] = '0'
		if int(''.join(bits), 3) < n:
			bits[i] = '1'
	
	print(int(''.join(bits), 3))