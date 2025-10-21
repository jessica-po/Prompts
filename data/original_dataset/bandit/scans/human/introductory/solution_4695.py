n1 = [1, 3, 5, 7, 8, 10, 12]
n2 = [4, 6, 9, 11]

a, b = list(map(int, input().split()))
print(("Yes" if a in n1 and b in n1 or a in n2 and b in n2 else "No"))