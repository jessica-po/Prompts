t = int(input())
for _ in range(t):
	x,y = map(int,input().split())
	a,b = map(int,input().split())
	wynik = 0
	if b <= 2*a:
		c = min(x,y)
		wynik += b*c
		wynik += (max(x,y)-c)*a
	else:
		wynik = a*(x+y)
	print(wynik)