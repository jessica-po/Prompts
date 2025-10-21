n = int(input())
moves = input()

turns_vasnja = int((len(moves)-1) / n)

count = 0
for i in range(1, turns_vasnja+1):
    if moves[n * i - 3] == moves[n * i - 2] == moves[n * i - 1]:
        count += 1

print(count)