X = int(input())

deposit = 100
y_later = 0

while deposit < X:
    y_later += 1
    deposit += deposit // 100

print(y_later)