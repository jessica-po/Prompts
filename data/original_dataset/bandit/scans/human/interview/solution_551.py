def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[1] - a[0] == a[2] - a[1]:
        d = a[1] - a[0]
        c1 = a[0]
        c2 = 'no'
        for i in range(3, n):
            if i * d + c1 == a[i]:
                pass
            elif c2 == 'no':
                c2 = a[i] - d * i
            elif i * d + c2 == a[i]:
                pass
            else:
                print('No')
                return
        if c2 == 'no':
            print('No')
        else:
            print('Yes')
        return
    else:
        f = True
        d = a[1] - a[0]
        c1 = a[0]
        c2 = a[2] - 2 * d
        #print(d, c1, c2)
        for i in range(3, n):
            if (a[i] == i * d + c1) or (a[i] == i * d + c2):
                pass
            else:
                f = False
                break
        if f:
            print('Yes')
            return
        f = True
        d = a[2] - a[1]
        c1 = a[1] - d
        c2 = a[0]
        #print(d, c1, c2)
        for i in range(3, n):
            if (a[i] == i * d + c1) or (a[i] == i * d + c2):
                pass
            else:
                f = False
                break
        if f:
            print('Yes')
            return
        f = True
        d = (a[2] - a[0]) / 2
        c1 = a[0]
        c2 = a[1] - d
        #print(d, c1, c2)
        for i in range(3, n):
            #print(a[i], i * d + c1, i * d + c2)
            if (a[i] == i * d + c1) or (a[i] == i * d + c2):
                pass
            else:
                f = False
                break
        if f:
            print('Yes')
        else:
            print('No')

main()