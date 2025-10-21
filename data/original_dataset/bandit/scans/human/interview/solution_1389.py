import sys



input       = []
input_index = 0

def next(type, number = None):
	def next():
		nonlocal input, input_index
		
		
		while input_index == len(input):
			if sys.stdin:
				input       = sys.stdin.readline().split()
				input_index = 0
			else:
				raise Exception()
				
				
		input_index += 1
		
		return input[input_index - 1]
		
		
	if number is None:
		result = type(next())
	else:
		result = [type(next()) for _ in range(number)]
		
	return result
	
	
	
n, m = next(int, 2)
iis = [next(str) for _ in range(n)]


count = 0
vs = [0] * n

for j in range(m - 1, -1, -1):
	for i in range(n - 1, -1, -1):
		c = iis[i][j]
		
		if c == "W" and vs[i] != 1:
			count += 1
			d = 1 - vs[i]
			
			for k in range(i + 1):
				vs[k] += d
		elif c == "B" and vs[i] != -1:
			count += 1
			d = -1 - vs[i]
			
			for k in range(i + 1):
				vs[k] += d
				
				
print(count)