n = int(input())
if n == 0:
	print('zero')
elif n == 1:
	print('one')
elif n == 2:
	print('two')
elif n == 3:
	print('three')
elif n == 4:
	print('four')
elif n == 5:
	print('five')
elif n == 6:
	print('six')
elif n == 7:
	print('seven')
elif n == 8:
	print('eight')
elif n == 9:
	print('nine')
elif n == 10:
	print('ten')
elif n == 11:
	print('eleven')
elif n == 12:
	print('twelve')
elif n == 13:
	print('thirteen')
elif n == 14:
	print('fourteen')
elif n == 15:
	print('fifteen')
elif n == 16:
	print('sixteen')
elif n == 17:
	print('seventeen')
elif n == 18:
	print('eighteen')
elif n == 19:
	print('nineteen')
else:
	if n // 10 == 2:
		res = 'twenty'
	elif n // 10 == 3:
		res = 'thirty'
	elif n // 10 == 4:
		res = 'forty'
	elif n // 10 == 5:
		res = 'fifty'
	elif n // 10 == 6:
		res = 'sixty'
	elif n // 10 == 7:
		res = 'seventy'
	elif n // 10 == 8:
		res = 'eighty'
	elif n // 10 == 9:
		res = 'ninety'

	if n % 10 == 1:
		res += '-one'
	elif n % 10 == 2:
		res += '-two'
	elif n % 10 == 3:
		res += '-three'
	elif n % 10 == 4:
		res += '-four'
	elif n % 10 == 5:
		res += '-five'
	elif n % 10 == 6:
		res += '-six'
	elif n % 10 == 7:
		res += '-seven'
	elif n % 10 == 8:
		res += '-eight'
	elif n % 10 == 9:
		res += '-nine'

	print(res)