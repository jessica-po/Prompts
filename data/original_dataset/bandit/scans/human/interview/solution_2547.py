# input = raw_input
# range = xrange
import sys
inp = [int(x) for x in sys.stdin.read().split()]; ii = 0

seg = [0]*200000

def offset(x):
	return x + 100000
def encode(x, y):
	return x*200002 + y
def decode(x):
	return x//200002, x%200002

def upd(node, L, R, pos, val):
	while L < R:
		seg[node] += val
		seg[offset(node)] += val*pos
		if L+1 == R:
			break
 
		M = (L+R)//2
		node <<= 1
		if pos < M:
			R = M
		else:
			L = M
			node += 1

def query(node, L, R, k):
	ret = 0
	while L < R:
		if k == 0:
			return ret
		if seg[node] == k:
			return ret + seg[offset(node)]
		if L+1 == R:
			return ret + k*L

		M = (L+R)//2
		node <<= 1
		if seg[node] >= k:
			R = M
		else:
			ret += seg[offset(node)]
			k -= seg[node]
			L = M
			node += 1

	return ret

n, m, k = inp[ii:ii+3]; ii += 3
A, B, both, neither = [], [], [], []
for i in range(n):
	t, a, b = inp[ii:ii+3]; ii += 3
	if a == 0 and b == 0:
		neither.append(encode(t, i+1))
	if a == 1 and b == 0:
		A.append(encode(t, i+1))
	if a == 0 and b == 1:
		B.append(encode(t, i+1))
	if a == 1 and b == 1:
		both.append(encode(t, i+1))
	upd(1, 0, 10001, t, 1)

A.sort(); B.sort(); both.sort()
p1 = min(k, len(both))
p2 = k - p1
if 2*k - p1 > m or p2 > min(len(A), len(B)):
	print(-1)
	return

sum, ans, ch = 0, 2**31, p1
for i in range(p1):
	sum += both[i]//200002
	upd(1, 0, 10001, both[i]//200002, -1)
for i in range(p2):
	sum += A[i]//200002 + B[i]//200002
	upd(1, 0, 10001, A[i]//200002, -1)
	upd(1, 0, 10001, B[i]//200002, -1)


ans = query(1, 0, 10001, m-2*k+p1) + sum

while p1 > 0:
	if p2 == min(len(A), len(B)):
		break
	upd(1, 0, 10001, A[p2]//200002, -1); sum += A[p2]//200002
	upd(1, 0, 10001, B[p2]//200002, -1); sum += B[p2]//200002
	upd(1, 0, 10001, both[p1-1]//200002, 1); sum -= both[p1-1]//200002
	p2 += 1
	p1 -= 1
	if m - 2*k + p1 < 0:
		break
	Q = query(1, 0, 10001, m-2*k+p1)
	if ans > sum + Q:
		ans = sum + Q
		ch = p1

print(ans)
ind = [both[i]%200002 for i in range(ch)] + [A[i]%200002 for i in range(k-ch)] + [B[i]%200002 for i in range(k-ch)]
st = neither + [both[i] for i in range(ch, len(both))] + [A[i] for i in range(k-ch, len(A))] + [B[i] for i in range(k-ch, len(B))]
st.sort()
ind += [st[i]%200002 for i in range(m-2*k+ch)]
print (' '.join(str(x) for x in ind))