t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    print(min((a+b)//3,a,b))