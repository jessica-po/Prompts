cards = list(map(int, input().split()))

result = sum(cards)

for i in range(5):
    cnt = cards.count(cards[i])
    cnt = min(cnt, 3)
    if cnt not in [2, 3]:
        continue
    result = min(result, sum(cards) - cnt * cards[i])

print(result)