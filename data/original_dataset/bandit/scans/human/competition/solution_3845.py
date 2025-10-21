A,B = list(map(int, input().split()))

S = [["." if h < 50 else "#" for _ in range(100) ] for h in range(100)]

end_black = False
for i in range(0,50,2):
    if end_black:
        break
    for j in range(100):
        if B <= 1:
            end_black = True
            break
        
        if j % 2 == 0:
            S[i][j] = "#"
            B -= 1


end_white = False
for i in range(53,100, 2):
    if end_white:
        break
    for j in range(100):
        if A <= 1:
            end_white = True
            break
        
        if j % 2 == 0:
            S[i][j] = "."
            A -= 1

print((100,100))
for i in range(100):
    print(("".join(S[i])))