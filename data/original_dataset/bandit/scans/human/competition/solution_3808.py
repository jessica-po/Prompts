n=int(input())
s=input()
stack=[]
for i in s:
	if i=="(":
		stack.append(i)
	elif i==")":
		if len(stack)>0:
			if (stack[-1]=="("):
				stack.pop()
			else:
				stack.append(")")
		else:
			stack.append(")")
if len(stack)==0:
	print ("Yes")
	return
if len(stack)==2:
	if stack[0]==")" and stack[1]=="(":
		print ("Yes")
		return
	else:
		print ("No")
		return
else:
	print ("No")