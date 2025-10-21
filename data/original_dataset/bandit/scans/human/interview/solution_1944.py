n = int(input())
arr = []
for i in range(n):
	a,b = map(int, input().split(' '))
	arr.append((a,b))
arr = sorted(arr)
for i in range(n-1):
	if(arr[i][1]>arr[i+1][1]):
		print("Happy Alex")
		break
else:
	print("Poor Alex")