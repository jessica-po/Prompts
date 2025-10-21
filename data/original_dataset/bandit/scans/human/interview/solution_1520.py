t = [0] * 26


def get_k(c):
    return ord(c) - ord('a')


def analyze(s):
    length_of_str = len(s)
    pos = 0
    beauty_table = [0] * 26
    for i in range(1, length_of_str):
        if s[i] != s[pos]:
            k = get_k(s[pos])
            beauty_table[k] = max(beauty_table[k], i - pos)

            pos = i
    k = get_k(s[pos])
    beauty_table[k] = max(beauty_table[k], length_of_str - pos)

    pos = 0
    while pos < length_of_str and s[pos] == s[0]:
        pos += 1
    left_beauty = pos
    pos = length_of_str - 1
    while pos > 0 and s[pos] == s[length_of_str - 1]:
        pos -= 1
    right_beauty = length_of_str - pos - 1
    return beauty_table, left_beauty, right_beauty


r = []
for _ in range(int(input())):
    p = input()
    if all(x == p[0] for x in p):  # pure
        k = get_k(p[0])
        for i in range(26):
            if i == k:
                t[i] = len(p) * (t[i] + 1) + t[i]
            else:
                t[i] = min(1, t[i])
    else:
        for i in range(26):
            t[i] = min(1, t[i])

        bt, lb, rb = analyze(p)
        lk, rk = get_k(p[0]), get_k(p[-1])

        if lk == rk:
            t[lk] = lb + rb + t[lk]
        else:
            t[lk], t[rk] = t[lk] + lb, t[rk] + rb
        for i in range(26):
            t[i] = max(t[i], bt[i])
    # r.append(max(t))
    # print('\ntableInfo: ', end= ' ')
    # for i in range(26):
    #     print('{}:{}/'.format(chr(i + ord('a')), t[i]), end=' ')
    # print('')
# print(' '.join(map(str, r)))
print(max(t))