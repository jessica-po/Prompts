r, g, b = map(int, input().split())
maxi = (r + g + b) // 3
print(min(maxi, r + g, r + b, g + b))