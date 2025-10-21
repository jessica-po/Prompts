x = input().split(' ')
if x[-1] == "month":
    if x[0] == '31':
        print(7)
    elif x[0] == '30':
        print(11)
    else:
        print(12)
else:
    if x[0] in ['5', '6']:
        print(53)
    else:
        print(52)