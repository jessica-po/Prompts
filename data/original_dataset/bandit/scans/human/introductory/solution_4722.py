A, B = map(int, input().split())
C = A + B

print("Possible" if A%3==0 or B%3==0 or C%3==0 else "Impossible")