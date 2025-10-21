x = int(input())

seq = list(map(int, input().split(' ')))

if seq == [0]:
    print("YES")
    print(0)

elif seq == [0, 0]:
    print("NO")

elif seq == [1, 0]:
    print("YES")
    print('1->0')

elif seq == [0, 0, 0]:
    print("YES")
    print("(0->0)->0")

elif seq == [1, 0, 0]:
    print("NO")

elif seq[x-1] == 1:
    print("NO")

#ENDS IN 1
    
elif seq[x-2] == 1:
    print("YES")

    print('->'.join([str(x) for x in seq]))


#ENDS IN 10

elif seq == [1] * (x-2) + [0, 0]:
    print("NO")

#000 BELOW
elif seq[x-3] == 0:
    a = ('->'.join([str(x) for x in seq][0:x-3]))
    print("YES")

    print(a + '->(0->0)->0')

#100
else:
    last = 0
    for i in range(x-1):
        if seq[i] == 0 and seq[i+1] == 1:
            last = i
    seq[last] = '(0'
    seq[last+1] = '(1'
    seq[x-2] = '0))'
    print("YES")
    print('->'.join([str(x) for x in seq]))