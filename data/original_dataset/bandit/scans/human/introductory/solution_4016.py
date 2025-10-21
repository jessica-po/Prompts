'''input
3 4
aba
'''
n, k = map(int, input().split())
t = input()
for i in range(1, n):
	if t[i:] == t[:n-i]:
		print(t[:i] * k + t[i:])
		break
else:
	print(t * k)