n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

fed_left = {0 : a[0]}
not_fed_left = {0 : b[0]}

for i in range(1, n):
	fed_left[i] = max(fed_left[i-1] + b[i], not_fed_left[i-1] + a[i]) # max(fed left, fed right)
	not_fed_left[i] = max(fed_left[i-1] + c[i], not_fed_left[i-1] + b[i]) # max(fed left and right, fed right)

print(fed_left[n-1])