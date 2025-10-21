n,c = list(map(int, input().split()))
P = list(map(int, input().split()))
T = list(map(int, input().split()))
a = 0
t = 0
for i in range(n):
    t += T[i]
    a += max(0,P[i]-c*t)
t = 0
b = 0
for i in range(n-1,-1,-1):
    t += T[i]
    b += max(0,P[i]-c*t)
if a > b:
    print("Limak")
elif a < b:
    print("Radewoosh")
else:
    print("Tie")