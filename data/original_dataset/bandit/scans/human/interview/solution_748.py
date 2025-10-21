def __starting_point():
    N = int(input())
    L = [0,0,0,0,0,0,0,0]
    inp = input()
    for i in inp.split(' '):
        L[int(i)]+=1
    it = N//3
    fnd = True
    ans = []
    for ic in range(it):
        Tl = []
        for el in range(len(L)):
            if L[el]!=0:
                if len(Tl)==0:
                    Tl.append(el)
                    L[el]-=1
                elif el%Tl[-1]==0:
                    Tl.append(el)
                    L[el]-=1
            if len(Tl)==3:
                break
        if len(Tl)==3:
            ans.append(str(Tl[0])+" "+str(Tl[1])+" "+str(Tl[2]))
        else:
            fnd=False
            break
    if fnd:
        for a in ans:
            print(a)
    else:
        print("-1")

            
    

__starting_point()