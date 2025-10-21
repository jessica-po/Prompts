a = 0
b = 0
x = {'Q': 9, 'q':9, 'R':5, 'r':5, 'B':3, 'b':3, 'N':3, 'n':3, 'P': 1, 'p': 1}
for i in range(8):
    t = [i for i in input()]
    for i in t:
        if ord(i) >= 97 and i in x:
            a += x[i]
        elif i in x:
            b += x[i]
if a == b:
    print("Draw")
elif a < b:
    print("White")
else:
    print("Black")