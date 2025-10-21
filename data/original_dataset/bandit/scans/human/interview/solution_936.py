n = int(input())
a = [int(x) for x in input().split()]
score = dict()
sup, winner = -2**31, None
for v in a:
    score[v] = score[v] + 1 if v in score else 1
    if score[v] > sup:
        sup, winner = score[v], v
print(winner)