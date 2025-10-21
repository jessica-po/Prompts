n = int(input())
d = list(map(int, input().split()))
s = {i:0 for i in [1, 2]}
for i in d:
	s[i] += 1
if s[2] >= s[1]:
	print(s[1])
else:
	print(s[2] + (s[1] - s[2]) // 3)