def modgroup(M = 10**9+7, invn = 0) :
	exec(f'''class mod{M} :
	inv = [None] * {invn}
	if {invn} >= 2 : inv[1] = 1
	for i in range(2, {invn}) : inv[i] = (({M}-{M}//i)*inv[{M}%i])%{M}
	def __init__(self, n = 0) : self.n = n % {M}
	__repr__ = lambda self : str(self.n) + '%{M}'
	__int__ = lambda self : self.n
	__eq__ = lambda a,b : a.n == b.n
	__add__ = lambda a,b : __class__(a.n + b.n)
	__sub__ = lambda a,b : __class__(a.n - b.n)
	__mul__ = lambda a,b : __class__(a.n * b.n)
	__pow__ = lambda a,b : __class__(pow(a.n, b.n, {M}))
	__truediv__ = lambda a,b : __class__(a.n * pow(b.n, {M-2}, {M}))
	__floordiv__ = lambda a,b : __class__(a.n * __class__.inv[b.n])
	''')
	return eval(f'mod{M}')
def solution() :
	s = input()
	l = len(s)
	mod = modgroup()
	num = [mod(0)] * (l+1) # num[i] = int(s[:i]) <mod>
	shift = [mod(1)] * (l+1) # shift[i] = 10**i <mod>
	for i,x in enumerate(s, 1) :
		num[i] = num[i-1] * mod(10) + mod(int(x))
		shift[i] = shift[i-1] * mod(10)
	def mod_check(la, lb, lc) :
		a,b,c = num[la], num[la+lb], num[la+lb+lc]
		c -= b * shift[lc]
		b -= a * shift[lb]
		return a + b == c
	for lc in range(l//3+bool(l%3), l//2+1) :
		for lb in (lc, lc-1, l-lc*2, l-lc*2+1) :
			la = l - lc - lb
			if la < 1 or lb < 1 or lc < 1 : continue
			if la > lc or lb > lc : continue
			if not mod_check(la, lb, lc) : continue
			a,b,c = s[:la], s[la:la+lb], s[la+lb:la+lb+lc]
			print(f'{a}+{b}={c}'); return
solution()