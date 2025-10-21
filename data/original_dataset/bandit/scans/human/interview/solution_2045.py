n = int(input())
words = input().split()[:n]

p_base = 1543
p_mod = 1300199

current = [c for c in words[0]]
for word in words[1:]:
    cur_hash = 0
    word_hash = 0
    cur_base = 1
    i_matches = []
    same_i = 0
    biggest_match = None
    while same_i < len(current) and same_i < len(word):
        cur_hash *= p_base
        cur_hash %= p_mod
        cur_hash += ord(current[len(current) - 1 - same_i])
        cur_hash %= p_mod

        word_hash += ord(word[same_i]) * cur_base
        word_hash %= p_mod

        cur_base *= p_base
        cur_base %= p_mod

        if cur_hash == word_hash:
            i_matches.append(same_i)
            #biggest_match = same_i

        same_i += 1


    for match in reversed(i_matches):
        if ''.join(word[:match + 1]) == ''.join(current[-1 - match:]):
            biggest_match = match
            break

    if biggest_match is None:
        current.extend(list(word))
    else:
        current.extend(list(word[biggest_match + 1:]))


print(*current, sep='')