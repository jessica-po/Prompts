n, k = list(map(int, input().split()))
s = list(input())
if len(s) == 1 and k:
	print(0)
	return
if s[0] != '1' and k:
	k -= 1
	s[0] = '1'
for i in range(1, len(s)):
	if s[i] != '0' and k:
		s[i] = '0'
		k -= 1
	if not k:
		break
print(''.join(s))