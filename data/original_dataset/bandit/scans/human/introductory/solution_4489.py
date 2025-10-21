def resolve():
    n = int(input())
    blue_cards = list()
    for i in range(n):
        card = input()
        blue_cards.append(card)
    blue_cards = sorted(blue_cards)
    m = int(input())
    red_cards = list()
    for i in range(m):
        card = input()
        red_cards.append(card)
    red_cards = sorted(red_cards)
    former = ""
    cards_points = []
    for card in blue_cards:
        point = 0
        if former == card:
            continue
        else:
            p = blue_cards.count(card)
            m = red_cards.count(card)
            point = p - m
            cards_points.append(point)
            former = card
    cards_points = sorted(cards_points)
    if cards_points[-1] < 0:
        print(0)
    else:
        print(cards_points[-1])
resolve()