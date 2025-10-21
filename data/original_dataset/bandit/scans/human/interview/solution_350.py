n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = arr[::-1]
ans = [arr[0]]
for i in range(1, n):
	if(arr[i] < ans[-1]):
		ans.append(arr[i])
	else:
		ans.append(max(0, ans[-1] - 1))
print(sum(ans))