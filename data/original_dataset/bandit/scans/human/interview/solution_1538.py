n = int(input())
d = list(map(int, input().split()))
s = {i:0 for i in set(d)}
for i in d:
	s[i] += 1
print(max(s.values()))