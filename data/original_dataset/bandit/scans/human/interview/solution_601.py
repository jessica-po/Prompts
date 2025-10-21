t = int(input())

for _ in range(t):
    p, f = [int(x) for x in input().split()]
    cs, cw = [int(x) for x in input().split()]
    s, w = [int(x) for x in input().split()]
    if s > w:
        s, w = w, s
        cs, cw = cw, cs

    best = 0
    for i in range(cs + 1):
        if s*i <= p:
            war_me = min((p - s*i)//w, cw)
            tb = i + war_me
            sword_him = min(cs - i, f//s)
            tb += sword_him
            war_him = min((f - s*sword_him)//w, cw - war_me)
            tb += war_him
            best = max(best, tb)
    print(best)