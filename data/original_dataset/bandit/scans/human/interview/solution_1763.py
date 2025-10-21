n, a, r, m = map(int, input().split())
h = list(map(int, input().split()))
m = min(m, a+r)

def get(M):
	up = 0
	dw = 0
	for e in h:
		if e > M:
			up += e - M
		else:
			dw += M - e
	ans = m * min(dw, up)
	if dw > up:
		ans += (dw - up) * a
	else:
		ans += (up - dw) * r
	return ans


L = 0
R = int(1e9)
mn = int(1e18)

while R - L > 10:
	M1 = L + (R - L) // 3
	M2 = R - (R - L) // 3
	V1 = get(M1)
	V2 = get(M2)
	mn = min(mn, V1)
	mn = min(mn, V2)
	if V1 < V2:
		R = M2
	elif V2 < V1:
		L = M1
	else:
		L = M1
		R = M2

for it in range(L, R+1):
	mn = min(mn, get(it))

print(mn)