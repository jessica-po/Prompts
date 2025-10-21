a, b = map(int,input().split())
i = 1
while 1:
    if a < i:
        print("Vladik")
        break
    a-= i
    i+= 1
    if b < i:
        print("Valera")
        break
    b-= i
    i+= 1