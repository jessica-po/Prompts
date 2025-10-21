def main():
	n, m, mn, mx = map(int, input().split())
	A = list(map(int, input().split()))
	a = min(A)
	b = max(A)
	if a < mn or b > mx:
		print("Incorrect")
		return
	cnt = 0
	if a > mn:
		cnt += 1
	if b < mx:
		cnt += 1
	if m + cnt <= n:
		print("Correct")
	else:
		print("Incorrect")

main()