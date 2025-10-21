w, r = open('output.txt', 'w'), open('input.txt', 'r')
s, y = [0] * 466, [0, 100, 131, 159, 190, 220, 251, 281, 312, 343, 373, 404, 434]
for i in range(int(r.readline())):
    m, d, p, t = map(int, r.readline().split())
    x = y[m] + d
    s[x] -= p
    s[x - t] += p
for i in range(465):
    s[i + 1] += s[i]
w.write(str(max(s)))