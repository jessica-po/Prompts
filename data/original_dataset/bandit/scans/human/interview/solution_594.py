n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = max(max(A), min(A) * 2)
if min(B) <= ans:
	print(-1)
else:
	print(ans)