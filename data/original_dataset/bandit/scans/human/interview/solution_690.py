N = input()
for digit in N[::-1]:
    Os = int(digit)%5
    if int(digit) >= 5:
        print("-O|"+Os*"O"+"-"+(4-Os)*"O")
    else:
        print("O-|"+Os*"O"+"-"+(4-Os)*"O")