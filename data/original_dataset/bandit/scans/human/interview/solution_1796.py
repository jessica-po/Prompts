str = input()
inpt = ""
n = int(str)
x = 0
for i in range(n):
	inpt = input()
	#print(inpt[0:2]+" - "+inpt[1:3])
	if(inpt[0:2] == "++" or inpt[1:3] == "++"):
		x += 1
		#print("x = {} plus 1".format(x))
	elif(inpt[0:2] == "--" or inpt[1:3] == "--"):
		x -= 1
		#print("x = {} minus 1".format(x))
print(x)