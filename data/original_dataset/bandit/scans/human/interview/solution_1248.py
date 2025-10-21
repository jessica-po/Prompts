d1, d2, d3 = map(int, input().split())
D1 = 2*d1 + 2*d2
D2 = d1 + d3 + d2
D3 = (d1 + d3) * 2
D4 = (d2 + d3) * 2
print(min(D1, D2, D3, D4))