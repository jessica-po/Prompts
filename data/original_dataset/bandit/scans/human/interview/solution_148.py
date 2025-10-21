n, a, x, b, y = map(int, input().split())

while a != x and b != y and a != b:
	if a == b:
		break

	a = a % n + 1
	b = b - 1 if b - 1 else n

print("YNEOS"[a != b::2])