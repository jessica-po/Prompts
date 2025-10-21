seat = input()
time_to = {'a': 4, 'f': 1, 'b': 5, 'e': 2, 'c': 6, 'd': 3}
col = seat[-1]
row = int(seat[:-1])
row -= 1

blocks_to_serve = row // 4
time = (6 * 2 + 4) * blocks_to_serve

if row % 2 == 1:
    time += 6 + 1

time += time_to[col]

print(time)