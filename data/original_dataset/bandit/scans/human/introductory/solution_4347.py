from math import *

n = int(input())
print(factorial(n) // (factorial(n // 2) ** 2) * factorial(n//2-1) ** 2 // 2)