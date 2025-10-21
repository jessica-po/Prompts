start = input()
counter = 0
sInt = int(start)
while sInt!=0:
	sInt-=max([int(c) for c in start])
	start=str(sInt)
	counter+=1
print(counter)