S = input()
K = int(input())

if len(S) == 1:
    print(S)
else:
    flg = False
    while S[0] == '1':
        S = S[1:]
        K -= 1

        if K == 0:
            print(1)
            flg = True
            break
    
    if not flg:
        if S[0] == '2':
            if K.bit_length() - 1 >= 5000000000000000:
                print(S[1])
            else:
                print(S[0])
        else:
            print(S[0])