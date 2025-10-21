t = int(input())
for _ in range(t):
	n = int(input())
	arr = [int(j) for j in input().split()]
	flag = 0
	for x in arr:
		if x%2 != arr[0]%2:
			flag = 1
			break
	if flag == 1:
		print("NO")
	else:
		print("YES")