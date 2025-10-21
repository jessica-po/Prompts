from collections import defaultdict

l = list(map(int, input().split()))
st = input()
s = [(ord(i) - ord('a')) for i in st]
track = [defaultdict(lambda: 0) for i in range(26)]
res = 0
s = [0] + s
pre = [0 for i in range(len(s))]
for i in range(1, len(s)):
	pre[i] = pre[i-1] + l[s[i]]
for i in range(1, len(s)):
	res += track[s[i]][pre[i-1]]
	track[s[i]][pre[i]] += 1
print(res)