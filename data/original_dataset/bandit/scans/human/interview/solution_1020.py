w, h, k = map(int, input().split())
ans = 0
for i in range(k):
	ans += w * 2 + (h - 2) * 2
	#print(ans, h, w)
	w -= 4
	h -= 4
print(ans)