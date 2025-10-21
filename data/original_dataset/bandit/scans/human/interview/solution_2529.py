x = list(map(float, input(" ").split()))
amount=int(x[0])
bal=float(x[1])
if amount+0.5 > bal or amount % 5 != 0:
    print("{:.2f}".format(bal))
else:
    bal = bal - amount-0.5
    print("{:.2f}".format(bal))