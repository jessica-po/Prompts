n = int(input())
k = input()
amount = 0
for elem in k:
    amount += 1
    if elem == '0':
        break
print(amount)