haiku = list(map(int, input().split()))
if haiku == [5, 5, 7] or haiku == [5, 7, 5] or haiku == [7, 5, 5]:
	print("YES")
else:
	print("NO")