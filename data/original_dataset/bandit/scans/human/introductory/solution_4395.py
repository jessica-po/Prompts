starts = ["RGB", "RBG", "BRG", "BGR", "GRB", "GBR"]

N = int(input())
s = input()

min_cost = float("inf")
min_str = ""

for k in starts:
	sp = (k * -(-N // 3))[:N]
	cost = sum(x != y for x, y in zip(s, sp))
	if cost < min_cost:
		min_cost = cost
		min_str = sp

print(min_cost)
print(min_str)