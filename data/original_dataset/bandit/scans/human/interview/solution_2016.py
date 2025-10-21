#!/usr/bin/env python3

# solution after hint
# (instead of best hit/mana spell store convex hull of spells)
# O(n^2) instead of O(n log n)


[q, m] = list(map(int, input().strip().split()))
qis = [tuple(map(int, input().strip().split())) for _ in range(q)]

mod = 10**6

j = 0
spell_chull = [(0, 0)]  # lower hull _/

def is_right(xy0, xy1, xy):
	(x0, y0) = xy0
	(x1, y1) = xy1
	(x, y) = xy
	return (x0 - x) * (y1 - y) >= (x1 - x) * (y0 - y)

def in_chull(x, y):
	i = 0
	if x > spell_chull[-1][0]:
		return False
	while spell_chull[i][0] < x:
		i += 1
	if spell_chull[i][0] == x:
		return spell_chull[i][1] <= y
	else:
		return is_right(spell_chull[i - 1], spell_chull[i], (x, y))
	


def add_spell(x, y):
	nonlocal spell_chull
	if in_chull(x, y):
		return
	i_left = 0
	while i_left < len(spell_chull) - 1 and not is_right(spell_chull[i_left + 1], spell_chull[i_left], (x, y)):
		i_left += 1
	i_right = i_left + 1
	while i_right < len(spell_chull) - 1 and is_right(spell_chull[i_right + 1], spell_chull[i_right], (x, y)):
		i_right += 1
	if i_right == len(spell_chull) - 1 and x >= spell_chull[-1][0]:
		i_right += 1
	spell_chull = spell_chull[:i_left + 1] + [(x, y)] + spell_chull[i_right:]


for i, qi in enumerate(qis):
	(k, a, b) = qi
	x = (a + j) % mod + 1
	y = (b + j) % mod + 1
	if k == 1:
		add_spell(x, y)
	else:  #2
		if in_chull(y / x, m / x):
			print ('YES')
			j = i + 1
		else:
			print ('NO')