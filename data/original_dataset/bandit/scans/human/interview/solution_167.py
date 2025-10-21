def get_substr_ends(haystack, needle):
	ans = [-1]
	index = 0
	for char in needle:
		while index < len(haystack) and char != haystack[index]:
			index += 1
		ans.append(index)
		if index < len(haystack):
			index += 1
	return ans

haystack = input()
needle = input()

pref = get_substr_ends(haystack, needle)
suff = get_substr_ends(haystack[::-1], needle[::-1])

pref_index = 0
suff_len = 0
while suff_len < len(suff) and suff[suff_len] < len(haystack):
	suff_len += 1

suff_len -= 1
best_str = needle[len(needle) - suff_len:]

if len(best_str) == len(needle):
	print(needle)
	return

for pref_len in range(1, len(pref)):
	while suff_len >= 0 and suff[suff_len] + pref[pref_len] + 2 > len(haystack):
		suff_len -= 1
	ans = pref_len + suff_len
	if ans > len(best_str) and suff_len >= 0:
		best_str = needle[:pref_len] + needle[len(needle) - suff_len:]

print(best_str if best_str else '-')