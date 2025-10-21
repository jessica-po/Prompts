for  testcases in range(int(input())):
	n,m = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	br = list(map(int, input().split()))
	flag = 0 
	ans = 0
	for i in ar:
		for j in br:
			if i == j :
				ans = i 
				flag = 1
				break
	if flag == 0 :
		print("NO")
	else:
		print("YES")
		print(1,ans)